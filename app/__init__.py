from flask import Flask
from app.views.user import user_page
from app.views.product import product_page
from app.views.update import itself_page
from app.extension import db
import os

app = Flask('app')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mysql@localhost/app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "lalskskskskksksjsj"

db.init_app(app)

app.register_blueprint(user_page)
app.register_blueprint(product_page)
app.register_blueprint(itself_page)

