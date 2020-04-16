from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mysql@localhost/app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
