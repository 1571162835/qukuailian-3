from flask import Flask
from app.views.user import user_page
from app.extension import db

app = Flask('first_flask')
app.config['SQLALCHEMY_DATABASE_URI'] = '数据库连接'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "lalskskskskksksjsj"

db.init_app(app)

app.register_blueprint(user_page)


