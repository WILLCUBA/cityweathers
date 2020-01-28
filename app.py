import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
@app.route('/')
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=cf64d91aa4cfb2d4f4a118b9eea69e60'
    city = 'Las Vegas'

    r = requests.get(url.format(city)).json()    
    print(r)

    return render_template('index.html')