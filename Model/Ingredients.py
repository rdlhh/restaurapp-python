class Ingredients:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.__product = {}

    def getName(self):
        return self.__name

    def getDesc(self):
        return self.__description

    def setName(self,name):
        self.__name = name
    
    def setDesc(self,desc):
        self.__description = desc

    def getOrder(self):
        return self.__product

    def setOrder(self,product):
        self.__product = product