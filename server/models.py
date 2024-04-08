
from flask_sqlalchemy import SQLAlchemy
from uuid import UUID

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users" #for table name
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(30)) #limit bycrypt password hash 30
    