class Ingredients:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description

    def getProdName(self):
        return self.__name

    def getProdDesc(self):
        return self.__description