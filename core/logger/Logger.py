import sys

class Logger():
    """description of class"""
    ## internal instance of the server
    __debug = True

    ## log item list        
    __log_items = []  

    ## project or software name associated to the project
    project_name = ""
    
    ## output file to flush the log informations
    export_file_name = ""

     
    ## add a new input into the logfile
    ## [in] logitem : instance of log item to add into the collection 
    def add(self, logitem):
        self.__log_items.append(logitem)
        if(True == self.__debug):
            print(logitem.getLine())

    # clear the current list of logfile    
    def clear(self):
        self.__log_items.clear()            



