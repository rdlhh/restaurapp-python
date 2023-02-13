import json
import requests
from Ingredients import Ingredients


class ControlIngredients:

    def __init__(self) -> None:
        self.__ingredients = {}

    def createIngredient(self, jason):
        response = requests.post("http://localhost:8069/restaurapp_app/addIngredients",json=jason).text
        response = json.loads(response)
        if response["result"]["status"] == 201:
            self.__ingredients[response["result"]["id"]] = Ingredients(jason["name"],jason["description"])
            return True
        else:
            return (response)

    def updateIngredient(self, jason):
        response = requests.put("http://localhost:8069/restaurapp_app/updateIngredients",json=jason).text
        response = json.loads(response)
        if response["result"]["status"] == 201:
            if "name" not in jason: jason["name"] = self.__ingredients[response["result"]["id"]].getName()
            if "description" not in jason: jason["description"] = self.__ingredients[response["result"]["id"]].getDesc()
            self.__ingredients[response["result"]["id"]] = Ingredients(jason["name"],jason["description"])
            return True
        else:
            return (response)

    def deleteIngredient(self, jason):
        response = requests.delete("http://localhost:8069/restaurapp_app/delIngredient",json=jason).text
        response = json.loads(response)
        if response["result"]["status"] == 200:
            del self.__ingredients[jason["id"]]
            return True
        else:
            return response

    def chargeIngredients(self):
        response = requests.request("GET", "http://localhost:8069/restaurapp_app/getIngredients")
        if response.status_code == 200:
            data = response.json()
            for num in range(len(data["data"])):
                id = data["data"][num]["id"]
                name=data["data"][num]["name"]
                desc = data["data"][num]["description"]
                c = Ingredients(name,desc)
                self.__ingredients[id] = c
        return self.__ingredients

    def getIngredients(self):
        return self.__ingredients

    def findIngredient(self, id):
        response = requests.request("GET", "http://localhost:8069/restaurapp_app/getIngredients/"+str(id))
        if response.status_code == 200:
            data = response.json()
            for num in range(len(data["data"])):
                if data["data"][num]["id"] in self.__ingredients: return self.__ingredients[data["data"][num]["id"]]
                else:
                    name = data["data"][num]["name"]
                    desc = data["data"][num]["description"]
                    c = Ingredients(name,desc)
                    self.__ingredients[id] = c
                    return c