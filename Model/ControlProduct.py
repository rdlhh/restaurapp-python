import requests, json
from Product import Product
import ControlCat,ControlIngredients

controlcat = ControlCat.ControlCat()
controlingredients = ControlIngredients.ControlIngredients()

class ControlProduct:
    def __init__(self) -> None:
        self.__menu = {}

    def getMenu(self):
        return self.__menu

    def getAllProducts(self):
        response = requests.request("GET", "http://localhost:8069/restaurapp_app/getProduct")
        if response.status_code == 200:
            data = response.json()
            for num in range(len(data["data"])):
                id = data["data"][num]["id"]
                name = data["data"][num]["name"]
                desc = data["data"][num]["description"]
                price = data["data"][num]["price"]
                c = Product(name,desc,price)
                c.setCategory(controlcat.findCategory(data["data"][num]["category"][0]))
                ingre = []
                for ing in range(len(data["data"][num]["ingredients"])):
                    ingre.append(controlingredients.findIngredient(data["data"][num]["ingredients"][ing]))
                c.setIngredients(ingre)
                self.__menu[id] = c
        return self.__menu

    def createProduct(self, jason):
        response = requests.post("http://localhost:8069/restaurapp_app/addProduct",json=jason).text
        response = json.loads(response)
        if response["result"]["status"] == 201:
            self.__menu[response["result"]["id"]] = Product(jason["name"],jason["description"],jason["price"])
            self.__menu[response["result"]["id"]].setCategory(controlcat.findCategory(jason["category"]))
            for ingre in range(len(jason["ingredients"])):
                self.__menu[response["result"]["id"]].getIngredients().append(controlingredients.findIngredient(jason["ingredients"][ingre]))
            return True
        else:
            return (response)

    def updateProduct(self, jason):
        response = requests.put("http://localhost:8069/restaurapp_app/updateProduct",json=jason).text
        response = json.loads(response)
        if response["result"]["status"] == 201:
            if "name" not in jason: jason["name"] = self.__menu[response["result"]["id"]].getName()
            if "description" not in jason: jason["description"] = self.__menu[response["result"]["id"]].getDesc()
            if "price" not in jason: jason["price"] = self.__menu[response["result"]["id"]].getPrice()
            if "category" not in jason: jason["category"] = self.__menu[response["result"]["id"]].getCategory()
            if "ingredients" not in jason: jason["ingredients"] = self.__menu[response["result"]["id"]].getIngredients()
            self.__menu[response["result"]["id"]] = Product(jason["name"],jason["description"],jason["price"])
            self.__menu[response["result"]["id"]].setCategory(controlcat.findCategory(jason["category"]))
            for ingre in range(len(jason["ingredients"])):
                self.__menu[response["result"]["id"]].getIngredients().append(controlingredients.findIngredient(jason["ingredients"][ingre]))
            return True
        else:
            return (response)

    def deleteProduct(self, jason):
        response = requests.delete("http://localhost:8069/restaurapp_app/delProduct",json=jason).text
        response = json.loads(response)
        if response["result"]["status"] == 200:
            del self.__menu[jason["id"]]
            return True
        else:
            return response

    def findProduct(self,id):
        response = requests.request("GET", "http://localhost:8069/restaurapp_app/getProduct/"+str(id))
        if response.status_code == 200:
            data = response.json()
            for num in range(len(data["data"])):
                if data["data"][num]["id"] in self.__menu: return self.__menu[data["data"][num]["id"]]
                else:
                    id = data["data"][num]["id"]
                    name=data["data"][num]["name"]
                    desc = data["data"][num]["description"]
                    price = data["data"][num]["price"]
                    c = Product(name,desc,price)
                    c.setCategory(controlcat.findCategory(data["data"][num]["category"][0]))
                    ingre = []
                    for ing in range(len(data["data"][num]["ingredients"])):
                        ingre.append(controlingredients.findIngredient(data["data"][num]["ingredients"][ing]))
                    c.setIngredients(ingre)
                    self.__menu[id] = c
                    return c