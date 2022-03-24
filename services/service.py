from injector import inject
import asyncio
# import aiofiles

from db.database import DatabaseBase

class Service:
    @inject
    def __init__(self, db: DatabaseBase):
        print(f"DatabaseBase instance is {db}")  # We want to see the object that gets created
        self.db = db

    def get_data(self):
        return asyncio.run(self.db.get())

    def get_git_data():
        pass
    def write_file(dic):
        f = open("foo.txt",'a')
        f.write(dic)
        f.flush()