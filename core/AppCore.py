from core.api.Connecter import Connecter
from core.logger.Logger import Logger
from core.logger.LogItem import LogItem
from core.api.UrlBuilder import UrlBuilder
from core.tools.SingletonMeta import SingletonMeta
## Factories for data
from core.api.factories.FactoryFreeCompany import FactoryFreeCompany

from core.AppController import AppController

class AppCore(metaclass=SingletonMeta):
    """description of class"""
    def TestRequest():
        AppController.logger.add(LogItem("[RequestApi][TEST][ENTER]"))
        data = AppController.connecter.Request("https://xivapi.com/item/1675")
        AppController.logger.add(LogItem("[RequestApi][TEST][DATA] - " + str(data)))
        AppController.logger.add(LogItem("[RequestApi][TEST][LEAVE]"))

    def RequestFreeCompanyData(id):
        AppController.logger.add(LogItem("[RequestApi][FC][ENTER]"))
        data = AppController.connecter.Request(UrlBuilder.getFreeCompanyRequest(id))
        AppController.FreeCompany = FactoryFreeCompany.setData(data)
        AppController.logger.add(LogItem("[RequestApi][FC][DATA] - " + str(data)))
        AppController.logger.add(LogItem("[RequestApi][FC][LEAVE]"))


