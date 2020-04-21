from .extension import db


class User(db.Model):
    """
    role:
        0-超级管理员，1-生产商，2-承运商，3-经销商
    """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), unique=False, nullable=False)
    role = db.Column(db.Integer, unique=False, nullable=False)
    real_name = db.Column(db.String(80), unique=False, nullable=True)
    tel = db.Column(db.String(20), unique=False, nullable=True)
    email = db.Column(db.String(120),unique=False, nullable=True)

    def __init__(self, username, password, role, real_name=None, tel=None):
        self.username = username
        self.password = password
        self.role = role
        self.real_name = real_name
        self.tel = tel

    def __repr__(self):
        return '<User %r>' % self.username


class Product(db.Model):
    """
    status:
        1-待运输，2-运输中，3-已到达
    """
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    number = db.Column(db.Integer, unique=False, nullable=False)
    dest = db.Column(db.String(100), unique=False, nullable=False)
    status = db.Column(db.Integer, unique=False, nullable=False)
    desc = db.Column(db.String(200), unique=False, nullable=True)

    def __init__(self, name, number, dest, status, desc=None):
        self.name = name
        self.number = number
        self.dest = dest
        self.status = status
        self.desc = desc

    def __repr__(self):
        return '<Product %r: %r>' % (self.id, self.name)
