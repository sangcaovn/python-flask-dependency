import json
from flask import Flask, request
from flask_injector import FlaskInjector
from injector import inject
from flask import render_template
from services.service import Service
from dependencies import configure
import asyncio


app = Flask(__name__)


@inject
@app.route('/data',methods=["POST"])
def get_data(service: Service):
    print(f"Service instance is {service}")  
    return service.get_data()


@inject
@app.route('/index')
def get_data_index(service: Service):
    print(f"Service instance is {service}")  
    return render_template(
        "index.html",
        data=service.get_data(),
    )

@inject
@app.route('/pokemon')
def get_data_pokemon(service: Service):
    print(f"Service instance is {service}")  
    result = asyncio.run(service.push_data_api_pokemon())
    print((result))
    return render_template(
        "index.html",
        data=result,
    )

@inject
@app.route('/weather')
def get_current_weather_data(service: Service):
    print(f"Service instance is {service}")  
    result = asyncio.run(service.get_current_weather())
    print((result))
    return render_template(
        "weather.html",
        data=result,
    )

@inject
@app.route('/user',methods=["POST", "GET"])
def get_user_info(service: Service):
    if request.method == "GET":
        return render_template("user_info.html")
    
    elif request.method == "POST":
        result = request.form
        data = asyncio.run(service.write_file(result))
        return render_template("user_data.html", data=data)

# Setup Flask Injector, this has to happen AFTER routes are added
FlaskInjector(app=app, modules=[configure])