from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bdae4da6880fcd039f4764a277497e24'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sitee.db'

db = SQLAlchemy(app)

from fitness import routes