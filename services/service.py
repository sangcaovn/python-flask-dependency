from injector import inject

from db.database import DatabaseBase

from flask import request

import asyncio,aiohttp,aiofiles,requests,json

class Service:
    @inject
    def __init__(self, db: DatabaseBase):
        print(f"DatabaseBase instance is {db}")  # We want to see the object that gets created
        self.db = db

    def get_data(self):
        return self.db.get()

    def get_git_data(self):
        pass

    def read_data_write_to_web(self):
        data_dict={}
        with open("foo.txt") as f:
            for line in f:
                (key, val) = line.split(':')
                data_dict[key] = val
        return data_dict

    def get_weather_data(self):
        #city_data = []
        # weather_data = {}
        str_site='https://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1'
        x = requests.get(str_site)
        weather_data = x.json()
        #weather_dict = {}
        city_name = x.json()["city"]['name']
        #weather_dict [x.json()["city"]['name']] = x.json()["list"]["weather"]["description"]
        #city_data.append(x.json()["city"]['name'])
        #weather_data.append(x.json()["list"]["weather"]["description"])
        # weather_data.update( {x.json()["city"]['name'] : x.json()["list"]["weather"]["description"]} )
        return weather_data['list'],city_name

    def write_file(self,data):
        f = open("foo.txt", "a")
        f.write(f'{data}')
        f.write(f'\n')
        f.close()

    def rewrite_file(self,data):
        f = open("foo.txt", "w")
        for k,v in data.items():
            f.write(f'{k}:{v}')
        f.close()

    def delete_data(self,remove_key):
        data_dict={}
        with open("foo.txt") as f:
            for line in f:
                (key, val) = line.split(':')
                data_dict[key] = val
            del data_dict[remove_key]
        return data_dict


