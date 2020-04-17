from flask import Blueprint, render_template, session, redirect, request, url_for, flash
import json
from app.extension import db
from ..models import User

user_page = Blueprint('user_page', __name__)


@user_page.route('/users/userlist')
def userlist():
    return render_template('users/userlist.html')

@user_page.route('/users/addlist')
def addlist():
    return render_template('/users/adduser.html')


@user_page.route('/thisuser')
def thisuser():
    user = User.query.filter_by(id=session.get('user_id')).first()
    js = json.dumps(user,default=user2dict)
    return js


@user_page.route('/adduser', methods=['GET', 'POST'])
def adduser():
    username = request.form.get('username')
    password = request.form.get('password')
    role = request.form.get('role')
    realname = '默认昵称'
    db.session.add(User(username,password,role,realname))
    db.session.commit()
    return render_template('/users/userlist.html')


@user_page.route('/')
@user_page.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('users/login.html')
    else:
        name = request.form.get('username')
        pwd = request.form.get('password')

        user = User.query.filter(User.username == name).first()

        if user and user.password == pwd:
            session['user_id'] = user.id
            return render_template('users/index.html')
        else:
            flash('登陆失败')
            return render_template('users/login.html')


@user_page.route('/findAll')
def findAll():
    print('调用findAll')
    users = User.query.all()
    print(users)
    users = [user2dict(user) for user in users]
    js = json.dumps(users)
    print(js)
    return js


@user_page.route('/deleteUser')
def deleteUser():
    username = request.args.get('username')
    print(username)
    db.session.delete(User.query.filter_by(username=username).first())
    db.session.commit()
    return render_template('/users/userlist.html')




def user2dict(User):
    return {
        'id':User.id,
        'username':User.username,
        'password':User.password,
        'email':User.email,
        'role':User.role
    }
