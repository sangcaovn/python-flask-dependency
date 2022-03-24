from injector import inject

from db.database import DatabaseBase

class Service:
    @inject
    def __init__(self, db: DatabaseBase):
        self.db = db

    def get_data(self):
        #return self.db.get()
        return self.db.get()

    def get_git_data():
        pass
    