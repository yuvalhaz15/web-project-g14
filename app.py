from flask import Flask, redirect, render_template
from flask import url_for
from flask import render_template
from datetime import timedelta
from flask import request, session, jsonify
import time
import requests
import asyncio
import aiohttp
from utilities.db.db_manager import dbManager
from settings import DB
import mysql.connector

app = Flask(__name__)
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)
app.config.from_pyfile('settings.py')



@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

