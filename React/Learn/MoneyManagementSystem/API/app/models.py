from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

class User(db.Model):
    __tablename__='user'
    userid=db.Column(db.String(500),primary_key=True)
    name=db.Column(db.String(500),nullable=False)
    email=db.Column(db.String(500),nullable=False)
    password=db.Column(db.String(500),nullable=False)
    