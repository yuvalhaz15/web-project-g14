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
from utilities.db.users_sign_up_db import usersSignUpDbManager

signUp = Blueprint('signUp', __name__,
                   static_folder='static',
                   static_url_path='/pages/signUp',
                   template_folder='templates')


@signUp.route('/user_sign_up')
def load_sign_up_page():
    cities_list = usersSignUpDbManager.get_cities_list()
    return render_template('SignUpPage.html', cities_list=cities_list, display_form=True)


@signUp.route('/user_sign_up_validation', methods=['GET', 'POST'])
def check_details_and_and_respone_respectively():
    if method == 'POST':
        email = request.form['email']
        if usersSignUpDbManager.email_is_exist(email):
            return render_template('SignUpPage.html', display_form=True, warning_meassage='האמייל שהוזן כבר קיים')
        password1 = request.form['password1']
        password2 = request.form['password2']
        if password1 != password2:
            return render_template('SignUpPage.html', display_form=True, warning_meassage='הסיסמאות אינן תואמות אנא נסה שנית')
        private_name=request.form['private_name']
        last_name = request.form['private_name']
        phone_number=request.form['phone_number']
        adress=request.form['adress']
        city=request.form['city']
        region=request.form['region']

        usersSignUpDbManager.add_user(email,password1,private_name,last_name,phone_number,adress,city,region)

        return render_template('SignUpPage.html', end_of_process_meassage='משתמש נוסף בהצלחה אנא התחבר על מנת להתחיל להנות מהאתר')
