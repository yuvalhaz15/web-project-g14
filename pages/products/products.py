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

products = Blueprint('products', __name__,
                         static_folder='static',
                         template_folder='templates')


@products.route('/products')
def load_products_page():
    return render_template('products.html')

@products.route('/products_all_categories')
def display_all_categories():
    products_to_display=productsDbManager.get_all_products()
    return render_template('products.html',products=products_to_display)