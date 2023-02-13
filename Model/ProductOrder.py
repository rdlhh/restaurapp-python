class productOrder:
    def __init__(self, product, quantity, price) -> None:
        self.__product = product
        self.__quantity = quantity
        self.__price = price

    def getProduct(self):
        return self.__product

    def getQuantity(self):
        return self.__quantity
    
    def getPrice(self):
        return self.__price

    def setProduct(self,product):
        self.__product = product

    def setQuantity(self,quantity):
        self.__quantity = quantity
    
    def setPrice(self,price):
        self.__price = price