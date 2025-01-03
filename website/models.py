from .import db # "." means from init
from flask_login import UserMixin # provides methods like is_authenticated(), is_active(), and is_anonymous(), which help to implement the user authentication system more easily.
from sqlalchemy.sql import func




class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
   

    
    

   
"""
Flask-login requires a User model with the following properties:

1. has an is_authenticated() method that returns True if the user has provided valid credentials
2. has an is_active() method that returns True if the user account is active
3. has an is_anonymous() method that returns True if the current user is an anonymous user
4. has a get_id() method which, given a User instance, returns the unique ID for that object


UserMixin class provides the implementation of this properties. Its the reason 
you can call for example is_authenticated to check if login credentials provide 
is correct or not instead of having to write a method to do that yourself.

"""

    

class Product(db.Model):
    __tablename__ = 'Store1'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(10000))
    quantity = db.Column(db.Integer)
    price = db.Column(db.DECIMAL(precision=10, scale=2))
    
    #repr returns the object as string
    def __repr__(self):
        return f'<Product id={self.id} x={self.name} y={self.quantity}>'
   

class Product2(db.Model):
    __tablename__ = 'Store2'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(10000))
    quantity = db.Column(db.Integer)
    price = db.Column(db.DECIMAL(precision=10, scale=2))
