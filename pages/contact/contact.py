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
from utilities.db.contact_db import contactDbManager



contact = Blueprint('contact', __name__,
                         static_folder='static',
                          static_url_path='/contact',
                         template_folder='templates')

@contact.route('/contact/<string:page_state>')
def load_contact_page(page_state):
    if page_state == 'first_display':
      return render_template('ContactNotLogin.html')

    return render_template('Contact.html')

@contact.route('/contact_submit', methods=['GET', 'POST'])
def check_user_contact_and_respone_respectively():

    if request.form['subject']:
       message_subject=request.form['subject']
    
    content=request.form['user_text']
    user_id=session['user_id']
    contactDbManager.insert_message(user_id,content,message_subject)
    
    return render_template('Contact.html',sucsses_message="ההודעה נשלחה ניצור איתך קשר בהקדם האפשרי")
    
    