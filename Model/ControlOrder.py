import requests, json
from Order import Order
from ProductOrder import productOrder
import ControlProduct

controlProduct = ControlProduct.ControlProduct()

class ControlOrder:
    
     
    def __init__(self) -> None:
        self.__orders = {}

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

    def chargeTable(self):
        response = requests.request("GET", "http://localhost:8069/restaurapp_app/getOrder")
        if response.status_code == 200:
            data = response.json()
            for num in range(len(data["data"])):
                id = data["data"][num]["id"]
                numTable=data["data"][num]["table"]
                diners = data["data"][num]["pax"]
                waiter = data["data"][num]["waiter"]
                client = data["data"][num]["clients"]
                state = data["data"][num]["state"]
                c = Order(numTable,diners,waiter,client)
                orders = {}
                total = 0
                for order in data["data"][num]["orderLine"]:
                    orders[order] = ControlOrder.findOrder(order)
                    total = total + orders[order].getPrice()
                c.setOrder(orders)
                c.setState(state)
                c.setTotal(total)
                self.__orders[id] = c
        return self.__orders