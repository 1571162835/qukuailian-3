from flask import Blueprint, render_template, session, redirect, request, url_for, flash
import json
from app.extension import db
from ..models import User

user_page = Blueprint('user_page', __name__)


@user_page.route('/users/addlist')
def addlist():
    userName = session['userName']
    return render_template('/users/user-add.html',username=userName)


@user_page.route('/users/index')
def userlist():
    userName = session['userName']
    return render_template('/users/main.html',username=userName)


@user_page.route('/thisuser')
def thisuser():
    userName = session['userName']
    user = User.query.filter_by(id=session.get('user_id')).first()
    js = json.dumps(user, default=user2dict)
    return js


@user_page.route('/adduser', methods=['GET', 'POST'])
def adduser():
    print('调用addUser')
    userName = session['userName']
    username = request.form.get('username')
    password = request.form.get('password')
    role = request.form.get('role')
    realname = request.form.get('real_name')
    db.session.add(User(username,password,role,realname))
    db.session.commit()
    return redirect(url_for('user_page.findAll',page=1))


@user_page.route('/')
@user_page.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('users/login.html')
    else:
        name = request.form.get('username')
        pwd = request.form.get('password')

        user = User.query.filter(User.username == name).first()
        print (user)

        if user and user.password == pwd:
            session['user_id'] = user.id
            session['userName'] = user.username;
            userName=session['userName']
            return render_template('users/main.html',username=userName)
        else:
            flash('登录失败')
            return render_template('users/login.html')


@user_page.route('/findAll/<int:page>', methods=['POST', 'GET'])
def findAll(page):
    print('调用findAll')
    pagination = User.query.filter(User.role != 0).paginate(page=page, per_page=2, error_out=False)
    userName = session['userName']
    return render_template('users/user-list.html', users=pagination.items,username = userName,pagination = pagination)
    # print(users)
    # users = [user2dict(user) for user in users]
    # js = json.dumps(users)
    # print(js)
    # return js


@user_page.route('/findUserByUsername/<int:page>',methods=['POST'])
def findUserByUsername(page):
    username = request.form.get('username')
    print(username)
    pagination = User.query.filter_by(username=username).paginate(page=page, per_page=2, error_out=False)
    return render_template('users/user-list.html', users=pagination.items,username = session['userName'],pagination=pagination)


@user_page.route('/deleteUser')
def deleteUser():
    username = request.args.get('username')
    print(username)
    db.session.delete(User.query.filter_by(username=username).first())
    db.session.commit()
    return redirect(url_for('user_page.findAll',page=1))


@user_page.route("/medituser/<id>", methods=['POST', 'GET'])
def medituser(id):
    userName = session['userName']
    user = User.query.get(id)
    if request.method == 'GET':
        return render_template('/users/user-modify.html', user=user,username=userName)
    else:
        username = request.form.get("username")
        role = request.form.get("role")
        password = request.form.get("password")
        user.username = username
        user.role = role
        user.password = password
        db.session.commit()
        return redirect(url_for('user_page.findAll',page=1))



@user_page.route("/logout", methods=['POST', 'GET'])
def logout():
    userName = session['userName']
    return render_template('users/login.html',username=userName)



def user2dict(User):
    return {
        'id':User.id,
        'username':User.username,
        'password':User.password,
        'email':User.email,
        'role':User.role
    }
