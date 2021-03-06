from core.api.Connecter import Connecter
from core.logger.Logger import Logger
from core.logger.LogItem import LogItem
from core.api.UrlBuilder import UrlBuilder
from core.tools.SingletonMeta import SingletonMeta
## Factories for data
from core.api.factories.FactoryFreeCompany import FactoryFreeCompany
from core.api.factories.FactoryMemberAchievements import FactoryMemberAchievements

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
        if(AppController.database.isFreeCompanyTable() == False):
            data = AppController.connecter.Request(UrlBuilder.getFreeCompanyRequest(id))
            AppController.database.addDataFreeCompany(data)
        else:
            data = AppController.database.getDataFreeCompany()
        AppController.FreeCompany = FactoryFreeCompany.setData(data)
        AppController.logger.add(LogItem("[RequestApi][FC][LEAVE]"))
        
    def RequestAchievementsMember(id):
        AppController.logger.add(LogItem("[RequestApi][AC][ENTER]"))
        data = AppController.connecter.Request(UrlBuilder.getAchievementsMemberRequest(id))
        AppController.MemberAchievements = FactoryMemberAchievements.setData(data)
        AppController.logger.add(LogItem("[RequestApi][AC][LEAVE]"))

    def RequestAchievementsDetail(id):
        AppController.logger.add(LogItem("[RequestApi][ACD][ENTER]"))
        data = AppController.connecter.Request(UrlBuilder.getRequestAchievementsDetail(id))
        AppController.AchievementsDetail = FactoryMemberAchievements.setDataDetails(data)
        AppController.logger.add(LogItem("[RequestApi][ACD][LEAVE]"))


