from typing import Dict

from aiohttp import ClientSession
from injector import inject

from db.database import DatabaseBase


class Service:
    @inject
    def __init__(self, db: DatabaseBase):
        print(f"DatabaseBase instance is {db}")  # We want to see the object that gets created
        self.db = db

    async def get_weather_data(self) -> Dict:
        weather_url = "https://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1"
        async with ClientSession() as session:
            async with session.get(weather_url) as response:
                weather_data = await response.json()

        return weather_data.get("list")

    def get_data(self):
        return self.db.get()

    def get_git_data(self):
        pass
