from flask import Flask, redirect, render_template, url_for, Blueprint
from flask import request, session, jsonify
from datetime import timedelta
import time
import requests
import asyncio
import aiohttp

from utilities.db.db_manager import dbManager
from settings import DB
import mysql.connector

from pages.about.about import about
from pages.homepage.homepage import homepage
from pages.contact.contact import contact
from pages.products.products import products
from pages.userPage.userPage import userPage
from pages.signUp.signUp import signUp



app = Flask(__name__)
UPLOAD_FOLDER='static/media/product/'

app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config.from_pyfile('settings.py')

# Homepage
app.register_blueprint(homepage)


## About
app.register_blueprint(about)


## Contact

app.register_blueprint(contact)



## products

app.register_blueprint(products)

## signUp

app.register_blueprint(signUp)

# sign_in/Up

app.register_blueprint(userPage)

