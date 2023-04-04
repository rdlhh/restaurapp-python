import json
import requests
from Category import Category

class ControlCat:

    def __init__(self) -> None:
        self.__categories = {}

    def createCategory(self, jason):
        response = requests.post("http://localhost:8069/restaurapp_app/addCat",json=jason).text
        response = json.loads(response)
        if response["result"]["status"] == 201:
            self.__categories[response["result"]["data"]] = Category(jason["name"])
            return True
        else:
            return (response)

    def updateCategory(self, jason): 
        response = requests.put("http://localhost:8069/restaurapp_app/updateCat",json=jason).text
        response = json.loads(response)
        if response["result"]["status"] == 200:
            if "name" not in jason: jason["name"] = self.__categories[response["result"]["id"]].getName()
            self.__categories[response["result"]["data"]] = Category(jason["name"])
            return True
        else:
            return (response)

    def deleteCategory(self, jason):
        response = requests.delete("http://localhost:8069/restaurapp_app/delCat",json=jason).text
        response = json.loads(response)
        if response["result"]["status"] == 200:
            del self.__categories[jason["id"]]
            return True
        else:
            return response

    def chargeCategories(self):
        response = requests.request("GET", "http://localhost:8069/restaurapp_app/category")
        if response.status_code == 200:
            data = response.json()
            for num in range(len(data["data"])):
                id = data["data"][num]["id"]
                name=data["data"][num]["name"]
                c = Category(name)
                self.__categories[id] = c
        return self.__categories

    def getCategories(self):
        return self.__categories

    def findCategory(self,id):
        response = requests.request("GET", "http://localhost:8069/restaurapp_app/getCategory/"+str(id))
        if response.status_code == 200:
            data = response.json()
            for num in range(len(data["data"])):
                if data["data"][num]["id"] in self.__categories: return self.__categories[data["data"][num]["id"]]
                else:
                    name = data["data"][num]["name"]
                    c = Category(name)
                    self.__categories[id] = c
                    return c