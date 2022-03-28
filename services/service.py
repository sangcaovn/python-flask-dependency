from injector import inject

from db.database import DatabaseBase

import asyncio
import aiohttp

class Service:
    @inject
    def __init__(self, db: DatabaseBase):
        print(f"DatabaseBase instance is {db}")  # We want to see the object that gets created
        self.db = db

    def get_data(self):
        return self.db.get()

    def get_git_data(self):
        pass

    def get_weather_data(self):
        weartherUrl = 'https://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1'
            weatherJson = resp.json()
                ls = weatherJson['list']
                return ls
