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



about = Blueprint('about', __name__,
                         static_folder='static',
                         template_folder='templates')

@about.route('/about')
def load_about_page():
    return render_template('about.html')