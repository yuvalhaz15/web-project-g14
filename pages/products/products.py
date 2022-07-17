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



products = Blueprint('products', __name__,
                         static_folder='static',
                         template_folder='templates')


@products.route('/products')
def load_products_page():
    return render_template('products.html')