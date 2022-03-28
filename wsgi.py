
from flask_injector import FlaskInjector
from injector import inject

from flask import Flask, render_template
from flask import request, redirect, url_for

from services.service import Service
from dependencies import configure


app = Flask(__name__)


@inject
@app.route('/')
def get_data_index(service: Service):
    print(f"Service instance is {service}")  # We want to see the object that gets created
    return render_template(
        "index.html",
        data=service.get_data(),
    )

@inject
@app.route('/weather')
def get_weather(service: Service):
    print(f"Service instance is {service}")  # We want to see the object that gets created
    weather,cityname=service.get_weather_data()
    return render_template(
        "weather.html",
        data=weather,
        cityname=cityname,
    )

@inject
@app.route('/form',methods = ['POST', 'GET'])
def load(service: Service):
    if request.method == 'POST':
        if request.form.get('Submit User') == 'Submit':
            result= {}
            fullname=''
            first_name = request.form.get("fname")
            last_name = request.form.get("lname") 
            age = request.form.get("age") 
            fullname = first_name + ' ' + last_name
            result[fullname] = age
            service.write_file(result)
        elif  request.form.get('Go to User List') == 'User List':
            return redirect("/user_list")
    return render_template(("form.html"))

@inject
@app.route('/user_list',methods = ['POST', 'GET'])
def post_web(service: Service):
    print(f"Service instance is {service}")  # We want to see the object that gets created
    if request.form.get('Go to User') == 'User':
        return redirect('/form')
    else:
        for i in service.read_data_write_to_web().keys():
            #print(i)
            if request.form.get('Delete User') == ('Delete '+i[2:-1]):
                print(request.form.get('Delete '+i[2:-1]))
                data=service.delete_data(i)
                service.rewrite_file(data)
    return render_template(
        "user_list.html",
        data=service.read_data_write_to_web(),
    )
    
# Setup Flask Injector, this has to happen AFTER routes are added
FlaskInjector(app=app, modules=[configure])