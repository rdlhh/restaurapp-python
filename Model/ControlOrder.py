import requests, json
from Order import Order
from ProductOrder import productOrder
import ControlProduct

controlProduct = ControlProduct.ControlProduct()

class ControlOrder:
     
    def __init__(self) -> None:
        pass

    def findOrder(self,id):
        response = requests.request("GET", "http://localhost:8069/restaurapp_app/getOrder/"+str(id))
        if response.status_code == 200:
            data = response.json()
            for num in range(len(data["data"])):
                product = controlProduct.findProduct(data["data"][num]["product"][0])
                quant = data["data"][num]["quantity"]
                price = data["data"][num]["price"]
                c = productOrder(product,quant,price)
                return c