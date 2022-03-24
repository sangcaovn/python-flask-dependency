import json
from flask import Flask, request
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


"""@inject
@app.route('/index')
def get_data_index(service: Service):
    print(f"Service instance is {service}")  # We want to see the object that gets created
    return render_template(
        "index.html",
        data=service.get_data(),
    )"""

@inject
@app.route('/weather')
def get_data_index(service: Service):
    print(f"Service instance is {service}")  # We want to see the object that gets created
    return render_template(
        "index.html",
        data=service.get_current_weather(),
    )

@inject
@app.route('/')
def submit():
   return render_template('submit.html')

@inject
@app.route('/result',methods = ['POST', 'GET'])
def result():
    dic = dict()
    if request.method == 'POST':
      result = request.form
      dic["Name"] = request.form.__getitem__('Name')
      dic["Physics"] = request.form.__getitem__('Physics')
      dic["chemistry"] = request.form.__getitem__('chemistry')
      dic["Mathematics"] = request.form.__getitem__('Mathematics')

    
      Service.write_data(dic)
      return render_template("result_of_submit.html",result = result)
    """if request.method == 'GET':
        result = request.form
        return Service.write_data(result)"""


# Setup Flask Injector, this has to happen AFTER routes are added
FlaskInjector(app=app, modules=[configure])