# from aiohttp import request
from flask import Flask,request
from flask_injector import FlaskInjector
from injector import inject
import json

from flask import render_template

from services.service import Service
from dependencies import configure

app = Flask(__name__)


@inject
@app.route('/data',methods=["POST","GET"])
# def get_data(service: Service):
def get_data(service: Service):
    dic = dict()
    # print(f"Service instance is {service}")  # We want to see the object that gets created
    # return service.get_data()
    dic['name'] = request.form.__getitem__('name')
    dic['age'] = request.form.__getitem__('age')
    Service.write_file(json.dumps(dic))
    return render_template("data.html")
    

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