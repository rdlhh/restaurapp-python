class Invoice:
    def __init__(self,id,ref,date,base,iva,total,state,lines, client):
        if id == None:
            self.__id = 0
        else:
            self.__id = id
        self.__ref = ref
        self.__date = date
        self.__base = base
        self.__iva = iva
        self.__total = total
        self.__state = state
        self.__lines = lines
        self.__client = client

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getRef(self):
        return self.__ref

    def setRef(self, ref):
        self.__ref = ref

    def getDate(self):
        return self.__date

    def setDate(self, date):
        self.__date = date

    def getBase(self):
        return self.__base

    def setBase(self, base):
        self.__base = base

    def getIva(self):
        return self.__iva

    def setIva(self, iva):
        self.__iva = iva

    def getTotal(self):
        return self.__total

    def setTotal(self, total):
        self.__total = total

    def getState(self):
        return self.__state

    def setState(self, state):
        self.__state = state

    def getLines(self):
        return self.__lines

    def setLines(self, lines):
        self.__lines = lines

    def getClient(self):
        return self.__client

    def setClient(self, client):
        self.__client = client