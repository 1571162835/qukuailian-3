from flask import Flask
from .views.user import user_page
from .extension import db

app = Flask('first_flask')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://tianji:tianji@127.0.0.1/python_admin'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = "lalskskskskksksjsj"

db.init_app(app)

app.register_blueprint(user_page)


