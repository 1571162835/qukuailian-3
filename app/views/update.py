from flask import Blueprint, render_template, request, session

from ..extension import db
from ..models import User
from werkzeug.security import generate_password_hash


itself_page = Blueprint('itself_page', __name__)


@itself_page.route('/user/detail/<username>')
def user_itself(username):
    user = User.query.filter(User.username == username).first()
    userName = session['userName']
    return render_template('users/user-detail.html', user=user, username=userName)


@itself_page.route('/user/modify/<int:user_id>', methods=['GET', 'POST'])
def user_modify(user_id):
    userName = session['userName']
    user = User.query.get(user_id)
    if request.method == 'GET':
        return render_template('users/user-update.html', user=user, username=userName)
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role')
        tel = request.form.get('tel')
        real_name = request.form.get('real_name')
        email = request.form.get('email')
        if password and tel and real_name and email:
            user.username, user.password, user.role, user.tel, user.real_name, user.email = username, generate_password_hash(password), role, tel, real_name, email
            db.session.commit()
            session['userName'] = user.username
            return str(user.username)
        else:
            return '0'
