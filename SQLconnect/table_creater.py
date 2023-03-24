import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from SQLconnect import DBconfig
from datetime import datetime

app = Flask(__name__)
ACCOUNTS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "accounts.json")
app.config.from_object(DBconfig)
db = SQLAlchemy(app)


# class Project(db.Model):
#     __tablename__ = 'project'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     url = db.Column(db.String(100), nullable=False)
#     name = db.Column(db.String(50), nullable=False)
#     account = db.Column(db.String(50), nullable=False)
#     password = db.Column(db.String(50), nullable=False)
#     accountXpath = db.Column(db.String(1000), nullable=False)
#     passwordXpath = db.Column(db.String(1000), nullable=False)
#     loginButton = db.Column(db.String(1000), nullable=False)
#     loginExtend = db.Column(db.JSON, nullable=True)
#     storage_time = db.Column(db.DateTime, default=datetime.now)

# class TestStep(db.Model):
#     __tablename__ = 'testStep'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     stepNo = db.Column(db.String(50), nullable=False)
#     title = db.Column(db.String(50), nullable=False)
#     elementPath = db.Column(db.String(1000), nullable=False)
#     actionDict = db.Column(db.JSON, nullable=False)
#     projectID = db.Column(db.Integer, nullable=False)
#     storage_time = db.Column(db.DateTime, default=datetime.now)
#
#
# class TestUnion(db.Model):
#     __tablename__ = 'testUnion'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     unionNo = db.Column(db.String(50), nullable=False)
#     name = db.Column(db.String(50), nullable=False)
#     runStep = db.Column(db.JSON, nullable=False)
#     projectID = db.Column(db.Integer, nullable=False)
#     storage_time = db.Column(db.DateTime, default=datetime.now)



if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.commit()
