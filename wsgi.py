from flask import Flask
from flask_injector import FlaskInjector
from injector import inject

from flask import render_template

from services.service import Service
from dependencies import configure

app = Flask(__name__)


@inject
@app.route('/data',methods=["POST"])
def get_data(service: Service):
    print(f"Service instance is {service}")  # We want to see the object that gets created
    return service.get_data()


@inject
@app.route('/index')
def get_data_index(service: Service):
    print(f"Service instance is {service}")  # We want to see the object that gets created
    return render_template(
        "index.html",
        data=service.get_data(),
    )

@inject
@app.route('/weather-forecast')
def get_data_weather(service: Service):
    print(f"Service instance is {service}")
    return render_template(
        "weather.html", 
        data=service.get_weather_data(),
    )    

# Setup Flask Injector, this has to happen AFTER routes are added
FlaskInjector(app=app, modules=[configure])