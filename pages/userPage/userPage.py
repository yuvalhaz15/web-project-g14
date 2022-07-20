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

userPage = Blueprint('userPage', __name__,
                     static_folder='static',
                     template_folder='templates')


@userPage.route('/user_login', methods=['GET', 'POST'])
def load_login_page():
    return render_template('userPage_signup.html')


@userPage.route('/user_login_validation', methods=['GET', 'POST'])
def check_user_login_request_and_respone_respectively():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

    if not usersDbManager.email_is_exist(email):
        return render_template('userPage_signup.html', message='כתובת המייל אינה קיימת אנא בדקו אותה')

    if not usersDbManager.password_is_correct(email, password):
        return render_template('userPage_signup.html', message='הסיסמא שהוזנה איננה נכונה')


    session['loged_in'] = True
    session['user_id']=usersDbManager.get_user_id(email)
    name_to_display = usersDbManager.get_user_name(email)
    return render_template('userPage_signup.html', user_name=name_to_display)


@userPage.route('/user_logout_validation')
def user_log_out():
 session['loged_in'] = False
 session['user_id']=None
 return render_template('userPage_signup.html')