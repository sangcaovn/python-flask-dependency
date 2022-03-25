from flask import Flask
from flask_injector import FlaskInjector
from injector import inject
from flask import redirect, url_for

from flask import render_template, request

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
def get_data_weather(service: Service):
    print(f"Service instance is {service}")  # We want to see the object that gets created
    return render_template(
        "weather.html",
        data=service.get_weather_data(),
    )

@inject
@app.route('/general-weather')
def get_general_data_weather(service: Service):
    print(f"Service instance is {service}")  # We want to see the object that gets created
    return render_template(
        "general_weather.html",
        data=service.get_general_weather_data(),
    )

@inject
@app.route('/user-info', methods=['GET', 'POST'])
def submit_user_form(service: Service):
    print(f"Service instance is {service}")  # We want to see the object that gets created
    if request.method == "POST":
        uuid = request.form['uuid']
        first_name = request.form['fname']
        last_name = request.form['lname']
        email = request.form['email']
        address = request.form['address']
        phone_number = request.form['phone']

        print("\nUUID is: ", uuid)
        print("\nFirst name is: ", first_name)
        print("\nLast name is: ", last_name)
        print("\nEmail is: ", email)
        print("\nAddress is: ", address)
        print("\nPhone Number: ", phone_number)

        dict_form = request.form.to_dict()
        print("Request: ", dict_form, " and its type: ", type(dict_form))
        print("JSON Format: ", dict_form)

        service.dump_into_json_file(dict_form)
        return redirect(url_for("get_users", users=Service.get_users()))
    
    return render_template(
        "user_form.html"
    )

@inject
@app.route('/user-info/<uuid>', methods=['GET', 'POST'])
def edit_user_form(service: Service, uuid):
    if request.method == "POST":
        dic_form = request.form.to_dict()
        update_success = service.update(uuid, dic_form)
        if update_success:
            print("Update user successfully!")
            return redirect(url_for("get_users", users=Service.get_users()))
        else:
            print('Update user failed!')

    print("\nReceived UUID: ", uuid)
    user_data = service.get_user(uuid)

    return render_template(
        "edit_user.html", user_data = user_data
    )

@inject
@app.route('/delete/user/<uuid>', methods=['GET'])
def remove_user(service: Service, uuid):
    del_sucess = service.delete(uuid)
    if del_sucess:
        return redirect(url_for("get_users", users=Service.get_users()))
    else:
        print("Delete user failed!")

@inject
@app.route('/users')
def get_users(service: Service):
    print(f"Service instance is {service}")  # We want to see the object that gets created
    return render_template(
        "users.html",
        users=Service.get_users(),
    )

# Setup Flask Injector, this has to happen AFTER routes are added
FlaskInjector(app=app, modules=[configure])