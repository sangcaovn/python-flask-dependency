from flask import Flask
from flask_injector import FlaskInjector
from injector import inject

from flask import render_template

from services.service import Service
from dependencies import configure
import requests
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
        demo="Hello"
    )

@app.route('/demo-render-html')
def demo_render_html(service: Service):
    response = requests.get("http://api.open-notify.org/astros.json").json()
    print(response)
    return render_template(
        "demo_render_html.html",
        data_render="HELLO DATA RENDER",
        data_service=service.get_data_service_to_render_html(),
        response=response
    )

@app.route('/weather-info')
def weather_info(service: Service):
    response = requests.get("https://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1").json()
    print(response)
    return render_template(
        "weather-info.html",
        weather_loop=response["list"]
    )

# Setup Flask Injector, this has to happen AFTER routes are added
FlaskInjector(app=app, modules=[configure])