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
        demo="Hello"
    )

@app.route('/demo-render-html')
def demo_render_html(service: Service):
    return render_template(
        "demo_render_html.html",
        data_render="HELLO DATA RENDER",
        data_service=service.get_data_service_to_render_html()
    )

# Setup Flask Injector, this has to happen AFTER routes are added
FlaskInjector(app=app, modules=[configure])