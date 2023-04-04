class Order:
    def __init__(self,id,table,client,state,waiter,price,lines):
        if id == None:
            self.__id = 0
        else:
            self.__id = id
        self.__table = table
        self.__client = client
        self.__state = state
        self.__waiter = waiter
        if price == None:
            self.__price = None
        else:
            self.__price = price
        if lines == None:
            self.__lines = None
        else:
            self.__lines = lines

    def setId(self,id):
        self.__id = id

    def getId(self):
        return self.__id

    def getTable(self):
        return self.__table
    
    def setTable(self,t):
        self.__table = t

    def getClient(self):
        return self.__client

    def setClient(self,c):
        self.__client = c

    def getState(self):
        return self.__state

    def setState(self,st):
        self.__state = st

    def getWaiter(self):
        return self.__waiter

    def setWaiter(self,w):
        self.__waiter = w

    def getPrice(self):
        return self.__price

    def setPrice(self,p):
        self.__price = p

    def getLines(self):
        return self.__lines

    def setLines(self,l):
        self.__lines = l