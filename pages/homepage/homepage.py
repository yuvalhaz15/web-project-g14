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



homePage = Blueprint('homePage', __name__,
                         static_folder='static',
                         static_url_path='/pages/homePage',
                         template_folder='templates')