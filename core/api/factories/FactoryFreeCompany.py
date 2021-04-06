from core.tools.SingletonMeta import SingletonMeta
from core.logger.Logger import Logger
## models
from core.api.models.FreeCompany import FreeCompany
from core.api.models.Estate import Estate
from core.api.models.Focus import Focus
from core.api.models.Ranking import Ranking
from core.api.models.Reputation import Reputation
from core.api.models.Seeking import Seeking
from core.api.models.FreeCompanyMembers import FreeCompanyMembers
## keys
from core.constants.KeysJson import KeysJson

class FactoryFreeCompany(metaclass=SingletonMeta):
    """description of class"""

    def setData(data):
        """
        Set data to free company object
        """
        freeCompany = FreeCompany()
        dataMembers =  data[KeysJson.FreeCompanyMembers]
        data = data[KeysJson.FreeCompany]
        
        freeCompany.Active = data[KeysJson.Active]
        freeCompany.ActiveMemberCount = data[KeysJson.ActiveMemberCount]
        freeCompany.Crest = data[KeysJson.Crest]
        freeCompany.DC = data[KeysJson.DC]

        estate = Estate()
        estate.Greeting = data[KeysJson.Estate][KeysJson.Greeting]
        estate.Name = data[KeysJson.Estate][KeysJson.Name]
        estate.Plot = data[KeysJson.Estate][KeysJson.Plot]
        freeCompany.Estate = estate

        focus = []
        for temp in data[KeysJson.Focus]:
            model = Focus()
            model.Icon = temp[KeysJson.Icon]
            model.Name = temp[KeysJson.Name]
            model.Status = temp[KeysJson.Status]
            focus.append(model)
        freeCompany.Focus = focus

        freeCompany.Formed = data[KeysJson.Formed]
        freeCompany.GrandCompany = data[KeysJson.GrandCompany]
        freeCompany.ID = data[KeysJson.ID]
        freeCompany.Name = data[KeysJson.Name]
        freeCompany.ParseDate = data[KeysJson.ParseDate]
        freeCompany.Rank = data[KeysJson.Rank]
        
        ranking = Ranking()
        ranking.Monthly = data[KeysJson.Ranking][KeysJson.Monthly]
        ranking.Weekly = data[KeysJson.Ranking][KeysJson.Weekly]
        freeCompany.Ranking = ranking
        
        freeCompany.Recruitment = data[KeysJson.Recruitment]

        reputation = []
        for temp in data[KeysJson.Reputation]:
            model = Reputation()
            model.Name = temp[KeysJson.Name]
            model.Progress = temp[KeysJson.Progress]
            model.Rank = temp[KeysJson.Rank]
            reputation.append(model)
        freeCompany.Reputation = reputation

        seeking = []
        for temp in data[KeysJson.Seeking]:
            model = Seeking()
            model.Icon = temp[KeysJson.Icon]
            model.Name = temp[KeysJson.Name]
            model.Status = temp[KeysJson.Status]
            seeking.append(model)
        freeCompany.Seeking = seeking

        freeCompany.Server = data[KeysJson.Server]
        freeCompany.Slogan = data[KeysJson.Slogan]
        freeCompany.Tag = data[KeysJson.Tag]

        freeCompanyMembers = []
        for temp in dataMembers:
            model = FreeCompanyMembers()
            model.Avatar = temp[KeysJson.Avatar]
            model.FeastMatches = temp[KeysJson.FeastMatches]
            model.ID = temp[KeysJson.ID]
            model.Lang = temp[KeysJson.Lang]
            model.Name = temp[KeysJson.Name]
            model.Rank = temp[KeysJson.Rank]
            model.RankIcon = temp[KeysJson.RankIcon]
            model.Server = temp[KeysJson.Server]
            freeCompanyMembers.append(model)
        freeCompany.FreeCompanyMembers = freeCompanyMembers

        return freeCompany



