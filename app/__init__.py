from sqlite3 import dbapi2
from flask import Flask
from  flask_sqlalchemy import SQLAlchemy
from os import path



    

DB_NAME = "database.db"



def create_up():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    db = SQLAlchemy(app)
    db.init_app(app)
   
   

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Pitch

    create_database(app)

   
    return app

def create_database(app):
    if not path.exists('app/' + DB_NAME):
        db.create_all(app=app)
        print('Created database')
