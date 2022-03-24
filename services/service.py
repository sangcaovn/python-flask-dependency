from select import select
from injector import inject
import asyncio

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

    def get_git_data():
        pass