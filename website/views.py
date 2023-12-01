from flask import Blueprint, redirect, render_template, request, flash, jsonify, url_for
from flask_login import login_required, current_user
from .models import Note,Product,User

from . import db
import json
import mysql.connector

views = Blueprint('views', __name__)



@views.route('/', methods=['GET', 'POST','DELETE']) 
@login_required
def home():

    all_users = User.query.all()       

    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

      

    return render_template("home.html", user=current_user,all_users=all_users)



@views.route('/store', methods=['GET', 'POST']) 
@login_required
def products():
 
    '''
    cursor = get_data().cursor()  #creates a cursor object that is associated with the database connection. The cursor is used to execute SQL queries and fetch results from the database.
    cursor.execute('SELECT * FROM PRODUCT')
    products = cursor.fetchall()  
    '''
    

    products = Product.query.all()      #MySQL Alchemy method
    
    
    return render_template("products.html", user=current_user, products = products )





'''The route where current product information is filled'''

@views.route('/edit_products', methods=['GET', 'POST'])
@login_required
def edit_products():
    
    if request.method == 'POST': 
        id = request.form.get('product_id')#Gets the product id from the HTML 
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
    
