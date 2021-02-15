from tinydb import TinyDB, Query
from core.tools.SingletonMeta import SingletonMeta

class DatabaseController(metaclass=SingletonMeta):
    """description of class"""

    dbFreeCompany = None

    def importDb():
        dbFreeCompany = TinyDB('database/data/dbFc.json')

