from core.api.Connecter import Connecter
from core.logger.Logger import Logger
from core.logger import LogItem
from core.api.UrlBuilder import UrlBuilder
from core.tools.SingletonMeta import SingletonMeta


from core.AppController import AppController

class AppCore(metaclass=SingletonMeta):
    """description of class"""
    def TestRequest():
        AppController.logger.add(LogItem.LogItem("[RequestApi][TEST][ENTER]"))
        data = AppController.connecter.Request("https://xivapi.com/item/1675")
        AppController.logger.add(LogItem.LogItem("[RequestApi][TEST][DATA] - " + str(data)))
        AppController.logger.add(LogItem.LogItem("[RequestApi][TEST][LEAVE]"))

    def RequestFreeCompanyData(id):
        AppController.logger.add(LogItem.LogItem("[RequestApi][FC][ENTER]"))
        data = AppController.connecter.Request(UrlBuilder.getFreeCompanyRequest(id))
        AppController.logger.add(LogItem.LogItem("[RequestApi][FC][DATA] - " + str(data)))
        AppController.logger.add(LogItem.LogItem("[RequestApi][FC][LEAVE]"))


