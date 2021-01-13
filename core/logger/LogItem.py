import datetime
from core.logger.EnuLogLevel import EnuLogLevel 
from core.logger.EnuLogOrigin import EnuLogOrigin

class LogItem:
    
    ## creation date time 
    logdate = None

    ## log item level 
    level = EnuLogLevel.Info

    ## log item origin
    origin = EnuLogOrigin.Unknown

    ## log item message value
    message = ""

    ## log stacktrace value
    stacktrace = ""

    ## constructor.        
    def __init__(self, message="", level=EnuLogLevel.Info, origin=EnuLogOrigin.Unknown, stacktrace="" ):
        self.logdate = datetime.datetime.now() 
        self.message = message
        self.level = level
        self.origin = origin
        self.stacktrace = stacktrace

    ## copy function from an existing instance of logitem
    ## [in] logitem : current intem to copy        
    def copy(self, logitem):
        self.logdate = logitem.logdate
        self.level = logitem.level
        self.origin = logitem.origin
        self.logdamessagete = logitem.message
        self.stacktrace = logitem.stacktrace

    ## getter on a formatted line of the current informations
    ## [return] formmated line to print log
    def getLine(self):
        return '{0}, {1}, {2}'.format(self.logdate, self.level, self.message)