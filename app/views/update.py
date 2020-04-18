from flask import Blueprint, render_template, request, session

from ..extension import db
from ..models import User


itself_page = Blueprint('itself_page', __name__)


@itself_page.route('/user/itself')
def user_itself():
    user_id = session['user_id']
    user = User.query.get(user_id)
    return render_template('users/itself.html', itself=user)


@itself_page.route('/user/modify/<int:user_id>', methods=['GET', 'POST'])
def user_modify(user_id):
    user = User.query.get(user_id)
    if request.method == 'GET':
        return render_template('users/modifyself.html', itself=user)
    else:
        password = request.form.get('password')
        tel = request.form.get('tel')
        real_name = request.form.get('real_name')
        email = request.form.get('email')
        if password and tel and real_name and email:
            user.password, user.tel, user.real_name, user.email = password, tel, real_name, email
            db.session.commit()
            return '1'
        else:
            return '0'
