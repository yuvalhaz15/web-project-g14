import os
import mysql.connector
from flask import Flask, Blueprint, render_template, request, redirect, jsonify
from flask import url_for
from datetime import timedelta
from flask import session
import requests
import asyncio
import aiohttp
from dotenv import load_dotenv
from utilities.db.products_db import productsDbManager
from utilities.db.products_crud_db import productsCrudDbManager
products = Blueprint('products', __name__,
                         static_folder='static',
                         template_folder='templates')


@products.route('/products')
def load_products_page():
    return redirect(url_for('products.display_all_categories'))

@products.route('/products_all_categories')
def display_all_categories():
    products_to_display=productsDbManager.get_all_products()
    return render_template('products.html',products=products_to_display)

@products.route('/products_by_category/<string:category>')
def display_spesific_categories(category):
    products_to_display=productsDbManager.get_category_products(category)
    return render_template('products.html',products=products_to_display)



@products.route('/user_products')
def display_user_products():
    products_to_display = productsDbManager.get_products_by_user_id(session['user_id'])
    return render_template('my_products.html', products=products_to_display)


##CRUD PRODUCT (TOY)

@products.route('/products_update_product/<string:page_state>', methods=['GET', 'POST'])
def update_products(page_state):
   if page_state == 'first_display':
     toys_id=productsCrudDbManager.get_products_id_by_user_id(session['user_id'])
     return render_template('my_products.html', update_product='true',toys_id=toys_id)

   toy_id = request.form['toy_id']
   toy_name = request.form['toy_name']
   toy_category = request.form['toy_category']
   toy_condition = request.form['toy_condition']
   productsCrudDbManager.update_product( toy_id, toy_name, toy_category, toy_condition)
   return render_template('my_products.html', message='הצעצוע עודכן בהצלחה')

@products.route('/products_delete_product/<string:page_state>')
def delete_products(page_state):
   if page_state == 'first_display':
     toys_id = productsCrudDbManager.get_products_id_by_user_id(session['user_id'])
     return render_template('my_products.html', delete_product='true', toys_id=toys_id)

   toy_id=request.args['toy_id']
   productsCrudDbManager.delete_product(toy_id)
   return render_template('my_products.html', message='הצעצוע נמחק בהצלחה')

@products.route('/products_add_product/<string:page_state>')
def add_products(page_state):
   if page_state == 'first_display':
     return render_template('my_products.html', add_product='true')

   toy_name = request.args['toy_name']
   toy_category = request.args['toy_category']
   toy_condition = request.args['toy_condition']
   productsCrudDbManager.add_product(session['user_id'],toy_name, toy_category, toy_condition)
   return render_template('my_products.html', message='הצעצוע נוסף בהצלחה')
