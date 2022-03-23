from injector import inject

from db.database import DatabaseBase

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