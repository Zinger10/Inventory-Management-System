from flask import Blueprint, redirect, render_template, request, flash, jsonify, url_for
from flask_login import login_required, current_user
from .models import Product2,User

from . import db
import json


views2 = Blueprint('views2', __name__)


#Act as file for table  2 operations



# Query all tables and send to products2.html page. Then table 2 is displayed
@views2.route('/store2', methods=['GET', 'POST']) 
@login_required
def products():
 
    '''
    cursor = get_data().cursor()  #creates a cursor object that is associated with the database connection. The cursor is used to execute SQL queries and fetch results from the database.
    cursor.execute('SELECT * FROM PRODUCT')
    products = cursor.fetchall()  
    '''
    
      

    product2s = Product2.query.all()      #MySQL Alchemy method
    
    tablename2 = Product2.__tablename__
    return render_template("products2.html", user=current_user, product2s = product2s , tablename2=tablename2 )





'''The route where current product information is filled'''

#edit backend for table 2.
@views2.route('/edit_products2', methods=['GET', 'POST'])
@login_required
def edit_products():
    
    if request.method == 'POST': 
        id = request.form.get('product_id')#Gets the product id from the HTML 
        product2 = Product2.query.filter_by(id=id).first()

        

    

        
        
    return render_template("edit2.html", product2 = product2 , user = current_user)
    
  
#Product updated and redirect user to views.products2.

@views2.route('/update2', methods=['GET', 'POST'])
@login_required
def update():
    #after pressing Save changes  
    if request.method == 'POST': 

        product_id = request.form.get('product_id')#Gets the product id from the HTML 
        new_quantity = int(request.form.get('amount'))#Gets the new amount from the HTML 

        product2 = Product2.query.filter_by(id=product_id).first() # # Retrieve the product from the database based on the ID 

        
        product2.quantity += new_quantity 

        db.session.commit()

        return redirect(url_for('views2.products'))

    

    


         

        
    return render_template("products2.html", user = current_user )
    

    



        

#adding product operations syntax. Don't mistake this with quantity only
@views2.route('/add2', methods=['POST'])
@login_required
def add():

    #data obtained from jsom
    product2 = json.loads(request.data)
    product_id2 = int(product2['id'])
    product_name2 = product2['name']
    product_price2 = product2['price']
    product_quantity2 = product2['quantity']

    new_product2 = Product2(id = product_id2, name = product_name2, price = product_price2, quantity = product_quantity2)


    db.session.add(new_product2)
    db.session.commit()

    

    return jsonify({})

@views2.route('/delete2', methods=['POST'])
@login_required
def delete():

    product_id2 = request.form.get('product_id')#Gets the product id from the HTML 

    product2 = Product2.query.filter_by(id=product_id2).first() # # Retrieve the product from the database based on the ID 

        
 
    db.session.delete(product2)
    db.session.commit()

    return redirect(url_for('views2.products'))


@views2.route('/get_chart_data2')
def get_chart_data():
    # Fetching data from the database
    data2 = Product2.query.all()

    # Processing data
    labels2 = [row.name for row in data2]
    values2 = [row.quantity for row in data2]

    # Prepare data to send as JSON
    chart_data2 = {'labels': labels2, 'values': values2}
    return jsonify(chart_data2)