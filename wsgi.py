from csv import list_dialects
from flask import Flask
from flask_injector import FlaskInjector
from injector import inject

from flask import render_template, request, jsonify

from services.service import Service
from dependencies import configure
import requests

import aiohttp
import asyncio
import os
import json
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

@app.route('/weather-info-2')
def weather_info2(service: Service):
    response = service.get_weather_api()
    # print(response)
    main = []
    for each_list in response["list"]:
        main.append(each_list["main"])
    # print(main)
    return render_template(
        "weather-info-2.html",
        cod=response["cod"],
        message=response["message"],
        cnt=response["cnt"],
        city=response["city"]["name"],
        main=main
    )

@app.route('/weather_use_aio')
def weather_use_aiohttp(service: Service):
    response = asyncio.run(service.call_api_use_io_service())
    main = []
    for each_list in response["list"]:
        main.append(each_list["main"])
    # print(main)
    return render_template(
        "weather-info-2.html",
        cod=response["cod"],
        message=response["message"],
        cnt=response["cnt"],
        city=response["city"]["name"],
        main=main
    )

@app.route('/demo-form')
def demo_form(service: Service):
    return render_template(
        "form_json.html"
    )


@app.route('/submit-form', methods=["POST"])
def submit_form_handle(service: Service):
    data = request.form.to_dict(flat=False)

    print ("data form submit >>>",data)

    lst_data=None
    check = os.path.exists('./user-info/user_info.json')
    if(check):
        lst_data=asyncio.run(service.read_file())
        try:
            lst_data = json.loads(lst_data)
        except:
            lst_data = []
        # if lst_data:
        #     lst_data = json.loads(lst_data)
        # else:
        #     lst_data = []
    print("check lst_data = ", lst_data)
    print("check type(lst_data) = ", type(lst_data))
    # print("check data = ", data)
    lst_data.append(data)
    asyncio.run(service.write_json_file(json.dumps(lst_data)))
    list_render = asyncio.run(service.read_file())
    list_render = json.loads(list_render)
    print("list_render = ", list_render)
    print(type(list_render))
    return render_template(
        "list_user.html",
        list_render=list_render
    )


# Setup Flask Injector, this has to happen AFTER routes are added
FlaskInjector(app=app, modules=[configure])