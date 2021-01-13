from core.api.Connecter import Connecter
from core.logger.Logger import Logger
from core.logger import LogItem
from core.tools.SingletonMeta import SingletonMeta

from core.AppController import AppController

class AppCore(metaclass=SingletonMeta):
    """description of class"""
    def TestRequest():
        AppController.logger.add(LogItem.LogItem("[RequestApi][ENTER]"))
        data = AppController.connecter.Request("https://xivapi.com/item/1675")
        AppController.logger.add(LogItem.LogItem("[RequestApi][DATA] - " + str(data)))
        AppController.logger.add(LogItem.LogItem("[RequestApi][LEAVE]"))

    def RequestFreeCompanyData():



