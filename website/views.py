from flask import Blueprint, redirect, render_template, request, flash, jsonify, url_for
from flask_login import login_required, current_user
from .models import Product,Product2,User

from . import db
import json


views = Blueprint('views', __name__)


# Home Page
@views.route('/', methods=['GET', 'POST','DELETE']) 
@login_required
def home():

    # Call for all users but not necessary
    all_users = User.query.all()       

     # Call for table names
    tablename1 = Product.__tablename__
    tablename2 = Product2.__tablename__
    

    
    return render_template("home.html", user=current_user,all_users=all_users , tablename1 = tablename1 , tablename2 = tablename2)

#route to obtain chart data
@views.route('/get_chart_data')
def get_chart_data():
   

    data = Product.query.all()


    # Processing data
    # row is a temporary variable that returns the rows of data from SQL Alchemy Object
    labels = [row.name for row in data]
    values = [row.quantity for row in data]

    # Prepare data to send as JSON. Storing chart_data in python dictionaries format
    chart_data = {'labels': labels, 'values': values}

    #returns chart_data dictionary in jsonify format in response to http request from client.
    return jsonify(chart_data)


# route to display table of products
@views.route('/store', methods=['GET', 'POST']) 
@login_required
def products():
 
    
    # equivalent to SQL select
    products = Product.query.all()      #MySQL Alchemy method

    #calls the table name of the class Product
    tablename1 = Product.__tablename__
    
    return render_template("products.html", user=current_user, products = products , tablename1 = tablename1 )





'''The route where current product information is filled'''

@views.route('/edit_products', methods=['GET', 'POST'])
@login_required
def edit_products():
    
    if request.method == 'POST': 
        id = request.form.get('product_id')#Gets the product id from the HTML 

        #gets the first row of product that matches with the id obtained from html
        product = Product.query.filter_by(id=id).first()

        

    

        
        
    return render_template("edit.html", product = product , user = current_user)
    
  
@views.route('/update', methods=['GET', 'POST'])
@login_required
def update():
    #after pressing Save changes  
    if request.method == 'POST': 

        product_id = request.form.get('product_id')#Gets the product id from the HTML 
        new_quantity = int(request.form.get('amount'))#Gets the new amount from the HTML 

        product = Product.query.filter_by(id=product_id).first() # # Retrieve the product from the database based on the ID 

        
        product.quantity += new_quantity 

        db.session.commit()
        flash('Product is updated', category='product-true')
        return redirect(url_for('views.products'))

    

    


         

        
    return render_template("products.html", user = current_user )
    

    



        


@views.route('/add', methods=['POST'])
@login_required
def add():

    product = json.loads(request.data)

    product_id = int(product['id'])
    product_name = product['name']
    product_price = product['price']
    product_quantity = product['quantity']

    new_product = Product(id = product_id, name = product_name, price = product_price, quantity = product_quantity)


    db.session.add(new_product)
    db.session.commit()

    

    return jsonify({})

@views.route('/delete', methods=['POST'])
@login_required
def delete():

    product_id = request.form.get('product_id')#Gets the product id from the HTML 

    product = Product.query.filter_by(id=product_id).first() # # Retrieve the product from the database based on the ID 

        
 
    db.session.delete(product)
    db.session.commit()

    return redirect(url_for('views.products'))
'''

user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')

'''
