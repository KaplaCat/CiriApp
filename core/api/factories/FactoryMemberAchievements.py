from core.tools.SingletonMeta import SingletonMeta
from core.logger.Logger import Logger
## keys
from core.constants.KeysJson import KeysJson
## models
from core.api.models.Achievements import Achievements
from core.api.models.Achievement import Achievement
from core.api.models.AchievementsDetails import AchievementsDetails
from core.api.models.AchievementCategory import AchievementCategory

class FactoryMemberAchievements(metaclass=SingletonMeta):
    """description of class"""

    def setData(data):
        """
        Set data to Achievements object
        """
        achievements = Achievements()
        data = data[KeysJson.Achievements]

        list = []
        for temp in data[KeysJson.List]:
            model = Achievement()
            model.Date = temp[KeysJson.Date]
            model.ID = temp[KeysJson.ID]
            list.append(model)
        achievements.Achieve = list

        achievements.Points = data[KeysJson.Points]

        return achievements

    def setDataDetails(data):
        """
        Set data to AchievementsDetails object
        """
        achievementsDetails = AchievementsDetails()

        achievementCategory = AchievementCategory()
        achievementCategory.ID = data[KeysJson.AchievementCategory][KeysJson.ID]
        achievementCategory.Name = data[KeysJson.AchievementCategory][KeysJson.Name]
        achievementCategory.Name_fr = data[KeysJson.AchievementCategory][KeysJson.Name_fr]
        achievementCategory.Order = data[KeysJson.AchievementCategory][KeysJson.Order]
        achievementsDetails.AchievementCategory = achievementCategory

        achievementsDetails.ClassJobRequirements = data[KeysJson.ClassJobRequirements]
        achievementsDetails.Data0 = data[KeysJson.Data0]
        achievementsDetails.Data1 = data[KeysJson.Data1]
        achievementsDetails.Data2 = data[KeysJson.Data2]
        achievementsDetails.Data3 = data[KeysJson.Data3]
        achievementsDetails.Data4 = data[KeysJson.Data4]
        achievementsDetails.Data5 = data[KeysJson.Data5]
        achievementsDetails.Data6 = data[KeysJson.Data6]
        achievementsDetails.Data7 = data[KeysJson.Data7]
        achievementsDetails.Description = data[KeysJson.Description]
        achievementsDetails.Description_fr = data[KeysJson.Description_fr]
        achievementsDetails.ID = data[KeysJson.ID]
        achievementsDetails.Icon = data[KeysJson.Icon]
        achievementsDetails.ItemTargetID = data[KeysJson.ItemTargetID]
        achievementsDetails.Item = data[KeysJson.Item]
        achievementsDetails.Name = data[KeysJson.Name]
        achievementsDetails.Name_fr = data[KeysJson.Name_fr]
        achievementsDetails.Order = data[KeysJson.Order]
        achievementsDetails.Patch = data[KeysJson.Patch]
        achievementsDetails.Points = data[KeysJson.Points]
        achievementsDetails.Title = data[KeysJson.Title]
        achievementsDetails.TitleTargetID = data[KeysJson.TitleTargetID]
        achievementsDetails.Type = data[KeysJson.Type]
        achievementsDetails.Url = data[KeysJson.Url]

        return achievementsDetails



        