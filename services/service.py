from importlib.resources import read_binary
from injector import inject

from db.database import DatabaseBase
import requests
import aiohttp
import aiofiles
import os.path
import json


class Service:
    @inject
    def __init__(self, db: DatabaseBase):
        # We want to see the object that gets created
        print(f"DatabaseBase instance is {db}")
        self.db = db

    def get_data(self):
        return self.db.get()

    def get_data_service_to_render_html(self):
        return "123"

    def get_git_data():
        pass

    def get_weather_api(self):
        response = requests.get(
            "https://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1").json()
        return response

    async def call_api_use_io_service(self):
        async with aiohttp.ClientSession() as session:
            weather_api = 'https://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1'
            async with session.get(weather_api) as resp:
                weather_response = await resp.json()
                return weather_response

    async def read_file(self):
        async with aiofiles.open('./user-info/user_info.json', mode='r') as f:
            contents = await f.read()
            print (contents)
            return contents if contents else []

    async def write_json_file(self, json_data):
        async with aiofiles.open('user-info/user_info.json', mode='w') as f:
            await f.write(json_data)

