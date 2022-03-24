from importlib.resources import read_binary
from injector import inject

from db.database import DatabaseBase
import requests
import aiohttp, aiofiles
import os.path

class Service:
    @inject
    def __init__(self, db: DatabaseBase):
        print(f"DatabaseBase instance is {db}")  # We want to see the object that gets created
        self.db = db

    def get_data(self):
        return self.db.get()

    def get_data_service_to_render_html(self):
        return "123"

    def get_git_data():
        pass

    def get_weather_api(self):
        response = requests.get("https://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1").json()
        return response

    async def call_api_use_io_service(self):
        async with aiohttp.ClientSession() as session:
            weather_api = 'https://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1'
            async with session.get(weather_api) as resp:
                weather_response = await resp.json()
                return weather_response

    async def read_files(self):
        async with aiofiles.open('user_info.json', mode='r') as f:
            contents = await f.read()
            return contents

    async def save_to_json(self, data):
        # print("Hello save_to_json")
        check = os.path.exists('./user_info.json')
        if check == False:
            async with aiofiles.open('user_info.json', mode='w') as f:
                await f.write("Hello world")
