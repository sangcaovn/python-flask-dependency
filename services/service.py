import json
from injector import inject
import aiohttp
from db.database import DatabaseBase

ACCESS_KEY='3c8c935347ffdcc8f4ffed8c8a887436'
class Service:
    @inject
    def __init__(self, db: DatabaseBase):
        print(f"DatabaseBase instance is {db}")  # We want to see the object that gets created
        self.db = db

    def get_data(self):
        return self.db.get()

    async def get_data_api(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1', ssl=False) as response:
                weather = await response.json()
                weather = weather["list"]
                return weather
    def get_git_data():
        pass