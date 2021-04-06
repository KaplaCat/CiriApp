from os import path
from tinydb import TinyDB, Query

class DatabaseController():
    """description of class"""
    def __init__(self):
        self.database = TinyDB('database/data/db.json', sort_keys=True, indent=4, separators=(',', ': '))
        self.tableFc = self.database.table('FreeCompany')

    ## Free Company Database
    def addDataFreeCompany(self,data):
        self.tableFc.insert(data)

    def updateDataFreeCompany(self,data):
        self.database.drop_table('FreeCompany')
        self.tableFc = self.database.table('FreeCompany')
        self.addDataFreeCompany(data)

    def getDataFreeCompany(self):
        return self.tableFc.all()[0]

    def isFreeCompanyTable(self):
        if(len(self.tableFc) == 0):
            return False
        return True




