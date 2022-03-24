from abc import ABC, abstractmethod
import json
import aiohttp
from injector import V

class DatabaseBase(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get(self):
        pass


class PostgresDatabase(DatabaseBase):
    def __init__(self):
        super().__init__()

    def connect(self):
        # TODO: implementation for a Postgres database connection
        print("Successfully connected to Postgres database!")

    async def get(self):
        # return "hello world!!!"  # Query the database here
        async with aiohttp.ClientSession() as session:
            weather_url = 'https://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1'
            async with session.get(weather_url,ssl=False) as resp:
                weather = await resp.json()
            
        return weather["list"]