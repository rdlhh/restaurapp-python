class Product:
    def __init__(self, name, description, photo, currency_id, price):
        self.__name = name
        self.__description = description
        self.__photo = photo
        self.__currency_id = currency_id
        self.__price = price
        self.__table = {}

    def getName(self):
        return self.__name

    def getDesc(self):
        return self.__description

    def getPrice(self):
        return self.__price

    