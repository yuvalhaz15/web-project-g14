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

def is_passwords_are_the_same(password1,password2):
    return password1==password2

@signUp.route('/user_sign_up')
def load_sign_up_page():
    cities_list = usersSignUpDbManager.get_cities_list()
    return render_template('SignUpPage.html', cities_list=cities_list, display_form=True)


@signUp.route('/user_sign_up_validation', methods=['GET', 'POST'])
def check_details_and_and_respone_respectively():
    if request.method == 'POST':
        cities_list = usersSignUpDbManager.get_cities_list()
        email = request.form['email']
        password1 = request.form['password1']
        password2 = request.form['password2']
        warning_meassage=None
        if usersSignUpDbManager.email_is_exist(email):
            warning_meassage = 'המייל שהוזן כבר קיים אנא נסה  אחר'


            
        elif not is_passwords_are_the_same(password1,password2):
            warning_meassage = 'הסיסמאות אינן תואמות אנא נסה שנית'
            
        if warning_meassage:
            return render_template('SignUpPage.html', display_form=True, warning_meassage=warning_meassage,
                                   cities_list=cities_list)
        
        private_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        adress = request.form['adress']
        city = request.form['city']
        print(city)
        region = request.form['region']

        usersSignUpDbManager.add_user(email, password1, private_name, last_name, phone_number, adress, city, region)

        return render_template('SignUpPage.html',
                               end_of_process_meassage='המשתמש נוסף בהצלחה אנא התחבר על מנת להתחיל להנות מהאתר')
