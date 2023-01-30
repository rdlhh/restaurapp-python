class Order:
    def __init__(self,table,diners,waiter,client) -> None:
        self.__table = table
        self.__client = client
        self.__waiter = waiter
        self.__diners = diners
        self.__total = 0
        self.__order = {}
        self.__state = "C"
        
    
    def getTableNum(self):
        return self.__table
    
    def setTableNum(self,table):
        self.__table = table

    def getOrder(self):
        return self.__order

    def setOrder(self,order):
        self.__order = order

    def getDiners(self):
        return self.__diners

    def setDiners(self,diners):
        self.__diners = diners

    def getWaiter(self):
        return self.__waiter

    def setWaiter(self,waiter):
        self.__waiter = waiter
    
    def getClient(self):
        return self.__client

    def setClient(self,client):
        self.__client = client

    def getTotal(self):
        return self.__total

    def setTotal(self,total):
        self.__total = total

    def getState(self):
        return self.__state

    def setState(self,state):
        self.__state = state