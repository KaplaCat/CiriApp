from core.api.Connecter import Connecter
from core.logger.Logger import Logger
from core.tools.SingletonMeta import SingletonMeta

class AppController(metaclass=SingletonMeta):
    """description of class"""

    # Connecter to get data from XIV Api
    connecter = Connecter()

    # Logger to Degug app
    logger = Logger()

    ## Data from API
    FreeCompany = -1
    MemberAchievements = -1
    AchievementsDetail = -1


