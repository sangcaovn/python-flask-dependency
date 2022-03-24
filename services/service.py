import json
import os
from injector import inject
import aiohttp
from db.database import DatabaseBase
import aiofiles

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
    async def sign_up(self, User):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        async with aiofiles.open(f'{dir_path}/data/user.json',mode = 'r') as file:
            user = []
            content = await file.read()
            if content != "":
                user = json.loads(content)
            user.append(User)
            async with aiofiles.open(f'{dir_path}/data/user.json', mode='w') as f:
                await f.write(json.dumps(user, indent=4))
            return user
    async def get_user(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        async with aiofiles.open(f'{dir_path}/data/user.json',mode = 'r') as file:
            content = await file.read()
            return content
        