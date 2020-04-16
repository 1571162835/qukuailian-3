from .extension import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    role = db.Column(db.Integer, unique=False, nullable=False)
    real_name = db.Column(db.String(80), unique=False, nullable=True)
    tel = db.Column(db.String(20), unique=True, nullable=True)

    def __init__(self, username, password, role, real_name=None, tel=None):
        self.username = username
        self.password = password
        self.role = role
        self.real_name = real_name
        self.tel = tel

    def __repr__(self):
        return '<User %r>' % self.username


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    number = db.Column(db.Integer, unique=False, nullable=False)
    dest = db.Column(db.String(100), unique=False, nullable=False)
    status = db.Column(db.Integer, unique=False, nullable=False)
    desc = db.Column(db.String(200), unique=False, nullable=True)

    def __init__(self, name, number, dest, status, desc=None):
        self.name = name
        self.number = number
        self.desc = dest
        self.status = status
        self.desc = desc

    def __repr__(self):
        return '<Product %r: %r>' % (self.id, self.name)
