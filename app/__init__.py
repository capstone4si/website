from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from app.utils import simpanGambar
app = Flask(__name__)
app.config['SECRET_KEY'] = 'abs'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/latiancapstone'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from app import routes



