# from aiohttp import request
from flask import Flask,request
from flask_injector import FlaskInjector
from injector import inject
import json

from flask import render_template

from services.service import Service
from dependencies import configure
import os
app = Flask(__name__)


@inject
@app.route('/data',methods=["POST","GET"])
# def get_data(service: Service):
def get_data(service: Service):

    # print(f"Service instance is {service}")  # We want to see the object that gets created
    # return service.get_data()
    if request.method == "POST" :
        data = {}
        data["name"] = request.form.__getitem__("name")
        data["age"] = request.form.__getitem__("age")
        if(os.path.exists("user/user.json")):
            lst = service.read_file("user/user.json")
        lst["list"].append(data)
        service.write_file(lst)
    else:
        pass
    return render_template("data.html")
    
@app.route("/route-two")
def route_two(service: Service):
    file = open('user/user.json','r')
    data = json.loads(file.read())
    print(f"Service instance is {service}")
    return render_template("route_two.html", data=data["list"])

@inject
@app.route('/index')
def get_data_index(service: Service):
    print(f"Service instance is {service}")  # We want to see the object that gets created
    return render_template(
        "index.html",
        data=service.get_data(),
    )

# Setup Flask Injector, this has to happen AFTER routes are added
FlaskInjector(app=app, modules=[configure])