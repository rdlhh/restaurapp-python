class Category:
    def __init__(self,name) -> None:
        self.__name = name
        self.__product = []

    def getName(self):
        return self.__name

    def setName(self,name):
        self.__name = name

    def getProduct(self):
        return self.__product

    def setProduct(self,prod):
        self.__product = prod