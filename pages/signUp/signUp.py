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
from utilities.db.users_db import usersDbManager



signUp = Blueprint('signUp', __name__,
                         static_folder='static',
                         static_url_path='/pages/signUp',
                         template_folder='templates')

@signUp.route('/user_sign_up')
def load_sign_up_page():
    return render_template('SignUpPage.html')

