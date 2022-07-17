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



homepage = Blueprint('homepage', __name__,
                         static_folder='static',
                         template_folder='templates')

@homepage.route('/')
def index():
  return redirect(url_for('homepage.load_home_page'))

@homepage.route('/homepage')
def load_home_page():
    return render_template('homepage.html')