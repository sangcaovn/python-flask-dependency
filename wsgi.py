from flask import Flask
from flask_injector import FlaskInjector
from injector import inject

from flask import render_template

from services.service import Service
from dependencies import configure

app = Flask(__name__)


@inject
@app.route('/data',methods=["GET"])
def get_data(service: Service):
    return service.get_data()


@inject
@app.route('/index')
def get_data_index(service: Service):
    return render_template(
        "index.html",
        data=service.get_data(),
    )

# Setup Flask Injector, this has to happen AFTER routes are added
FlaskInjector(app=app, modules=[configure])