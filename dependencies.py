from flask_injector import request

from db.database import DatabaseBase, PostgresDatabase
from services.service import Service


def configure(binder):
    binder.bind(DatabaseBase, to=PostgresDatabase, scope=request)
    binder.bind(Service, to=Service, scope=request)