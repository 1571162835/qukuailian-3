from flask import Flask
from app.views.user import user_page
from app.extension import db
import os

app = Flask('app')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "lalskskskskksksjsj"

db.init_app(app)

app.register_blueprint(user_page)


