import asyncio

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


@inject
@app.route('/index')
def get_data_index(service: Service):
    print(f"Service instance is {service}")  # We want to see the object that gets created
    return render_template(
        "index.html",
        data=service.get_data(),
    )
@inject
@app.route('/weather')
def get_data_url (service: Service):
    return render_template(
        "index.html",
        data=asyncio.run(service.get_data_api()),
    )
@inject
@app.route('/signup', methods = ['POST', 'GET'])
def submit_signup_form (service: Service):
    if (request.method == 'POST'):
        result = request.form
        result = asyncio.run(service.sign_up(result))

        return render_template('result.html', result = result)
    if (request.method == 'GET'):
        return render_template("signUp.html")
    

# Setup Flask Injector, this has to happen AFTER routes are added
FlaskInjector(app=app, modules=[configure])

