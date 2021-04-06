from core.tools.SingletonMeta import SingletonMeta
from core.constants.KeysApi import KeysApi

class UrlBuilder(metaclass=SingletonMeta):
    """description of class"""
    
    def getFreeCompanyRequest(id):
        return "https://xivapi.com/freecompany/"+ KeysApi.LODESTONE_ID_CL + "?data=FCM"
    
    def getAchievementsMemberRequest(id):
        return "https://xivapi.com/character/" + id + "?data=AC"

    def getRequestAchievementsDetail(id):
        return "https://xivapi.com/achievement/" + id


