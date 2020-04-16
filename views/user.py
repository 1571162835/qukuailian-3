from flask import Blueprint, render_template, session, redirect, request, url_for, flash
import json
from ..models import User

user_page = Blueprint('user_page', __name__)


@user_page.route('/users/list')
def list():
    return render_template('users/list.html')

@user_page.route('/addUser')
def addUser():
    if session.get('user_id'):
        uid = session.get('user_id')
        user = User.query.filter(User.id == uid).first()
        print('addUser已经执行')
        return json.dumps(user, default=user2dict)
    else:
        return redirect('/')


@user_page.route('/')
@user_page.route('/login', methods=['GET', 'PoSt'])
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


def user2dict(User):
    return {
        'id':User.id,
        'username':User.username,
        'password':User.password,
        'email':User.email,
        'role':User.role
    }
