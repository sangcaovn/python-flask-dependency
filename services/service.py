from select import select
from injector import inject
import asyncio
import json
import os
import uuid

from db.database import DatabaseBase

class Service:
    @inject
    def __init__(self, db: DatabaseBase):
        print(f"DatabaseBase instance is {db}")  # We want to see the object that gets created
        self.db = db

    def get_data(self):
        return asyncio.run(self.db.get()) 
    
    def get_weather_data(self):
        return asyncio.run(self.db.get_weather_data())

    def get_general_weather_data(self):
        return asyncio.run(self.db.get_general_weather_data())

    @staticmethod
    def parse_into_json_obj(filename):
        with open(filename, 'r') as openfile:
        # Reading from json file
            return json.load(openfile)

    def dump_into_json_file(self, json_obj):
        """If option is 1 we use dump otherwise use dumps"""
        dir_name = './user-info/'

        complete_path = Service.get_complete_path()
        # os.makedirs(complete_path)
        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)

        info = Service.parse_into_json_obj(complete_path)
        print(f"\nExisting data: {info}, with type {type(info)}\n")

        if len(info["list"]) > 0:
            info['list'].append(json_obj)
        else:
            info = {}
            info['list'] = [json_obj]

        if json_obj['uuid'] == '':
            user_uuid = str(uuid.uuid4()) 
            json_obj['uuid'] = user_uuid
            json_object = json.dumps(info, indent = 4)
            with open(complete_path, "w") as outfile:
                outfile.write(json_object)
            print(f'\nNew UUID = {user_uuid}, create a new record!')
        else:
            # update_user(user_uuid)
            pass

    @staticmethod
    def get_users():
        dir_name = './user-info/'
        filename = 'user.json'
        complete_path = os.path.join(dir_name, filename)

        return Service.parse_into_json_obj(complete_path)

    @staticmethod
    def get_complete_path():
        dir_name = './user-info/'
        filename = 'user.json'
        complete_path = os.path.join(dir_name, filename)

        return complete_path

    @staticmethod
    def get_user(uuid):
        list_users = Service.parse_into_json_obj(Service.get_complete_path())
        for user in list_users['list']:
            if user['uuid'] == uuid:
                return user
        
        return None

    def update(self, uuid, new_data):
        list_users = Service.parse_into_json_obj(Service.get_complete_path())
        pos = 0
        for user in list_users['list']:
            if user['uuid'] == uuid:
                user = new_data

                print(f'\nNew user data: {user}')
                # self.dump_into_json_file(list_users)
                list_users['list'][pos] = user
                list_users = json.dumps(list_users, indent = 4)
                with open(Service.get_complete_path(), "w") as outfile:
                    outfile.write(list_users)
                return True
            pos += 1

        return False

    def delete(self, uuid):
        list_users = Service.parse_into_json_obj(Service.get_complete_path())
        pos = 0
        for user in list_users['list']:
            if user['uuid'] == uuid:
                print(f'\nNew user data: {user}')
                # self.dump_into_json_file(list_users)
                del list_users['list'][pos]
                list_users = json.dumps(list_users, indent = 4)
                with open(Service.get_complete_path(), "w") as outfile:
                    outfile.write(list_users)
                return True
            pos += 1

        return False