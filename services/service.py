from injector import inject
import requests
from db.database import DatabaseBase

class Service:
    @inject
    def __init__(self, db: DatabaseBase):
        print(f"DatabaseBase instance is {db}")  # We want to see the object that gets created
        self.db = db

    def get_data(self):
        return self.db.get()

    def get_current_weather(self):
        url = "https://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1"
        data = requests.api.get(url)
        if(data.status_code):
            return data.json().get("list")
        return []

    def write_data(data):
        f = open("foo1.txt",'a')
        print(type(data))
        print(data)
        for key, value in data.items():
            f.write(f'{key}: {value}\n')
        f.flush()

    def get_git_data():
        pass