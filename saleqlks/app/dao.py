from app.models import LoaiPhong, Phong, TaiKhoan
from app import app, db
import hashlib


def load_categories():
    return LoaiPhong.query.all()


def load_products(kw=None, type_id=None):
    room = Phong.query

    if kw:
        room = room.filter(Phong.tenPhong.contains(kw))

    if type_id:
        room = room.filter(Phong.loaiphong_id.__eq__(type_id))

    return room.all()


def get_user_by_id(id):
    return TaiKhoan.query.get(id)


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return TaiKhoan.query.filter(TaiKhoan.username.__eq__(username.strip()),
                                 TaiKhoan.password.__eq__(password)).first()
