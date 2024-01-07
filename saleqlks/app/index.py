from flask import render_template, request, redirect, session, jsonify
import dao
import utils
from app import app, login
from flask_login import login_user


@app.route('/')
def index():
    kw = request.args.get('kw')
    type_id = request.args.get('type_id')

    type = dao.load_categories()
    room = dao.load_products(kw=kw, type_id=type_id)

    return render_template('index.html', categories=type, products=room)


@app.route('/products/<id>')
def details(id):
    return render_template('details.html')


@app.route('/admin/login', methods=['post'])
def login_admin_process():
    username = request.form.get('username')
    password = request.form.get('password')

    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user=user)

    return redirect('/admin')


def details(id):
    return render_template('details.html')


@app.route('/api/cart ', methods=['post'])
def add_cart():
    """
        {
        "cart": {
                "1": {
                    "id": 1,
                    "name": "ABC",
                    "price": 12,
                    "quantity": 2
                }, "2": {
                    "id": 2,
                    "name": "ABC",
                    "price": 12,
                    "quantity": 2
                }
            }
        }
        :return:
        """

    cart = session.get('cart')
    if cart is None:
        cart = {}

    data = request.json
    id = str(data.get("id"))

    if id in cart:  # phong da co trong gio
        cart[id]["quantity"] = cart[id]["quantity"] + 1
    else:  # phong chua co trong gio
        cart[id] = {
            "id": id,
            "name": data.get("name"),
            "price": data.get("price"),
            "quantity": 1
        }

    session['cart'] = cart

    return jsonify(utils.count_cart(cart))


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


@app.route("/login", methods=['get', 'post'])
def login_user_process():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user=user)

        next = request.args.get('next')
        return redirect("/" if next is None else next)

    return render_template('login.html')


if __name__ == '__main__':
    from app import admin

    app.run(debug=True)
