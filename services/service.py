from injector import inject

from db.database import DatabaseBase
import requests
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