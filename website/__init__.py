from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


def create_app():
  app = Flask(__name__) #This creates a Flask application object named app.

  app.config['SECRET_KEY'] = 'secret-key-goes-here'
  app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost:3306/bdp'
  db.init_app(app) # binds the database object to the flask app. Only then your flask app can do CRUD

  # blueprint for auth routes in our app
  from .auth import auth 
  app.register_blueprint(auth, url_prefix = '/')
  from .views import views
  app.register_blueprint(views, url_prefix = '/')
  
  from .models import User, Note, Product

    
  with app.app_context():
    db.create_all() #create database tables based on models.py

  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)

  @login_manager.user_loader
  def load_user(id):
    return User.query.get(int(id)) #The load_user function is responsible for taking that user ID and returning the corresponding User object from the database.

  
  return app

    
 



