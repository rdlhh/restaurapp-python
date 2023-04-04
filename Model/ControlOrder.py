import requests, json
from Order import Order
from orderLine import Line
import ControlProduct

controlProduct = ControlProduct.ControlProduct()

class ControlOrder:
    
    def getOrderById(self,id):
        url = "http://localhost:8069/restaurapp_app/getOrder/"+str(id)
        response = requests.request("GET", url)
        if response.status_code == 200:
            data = response.json()
        else:
            print("Error GET")
            return None

        json = {}
        json = data["data"]
        if(len(json) == 0):
            return None
        else:
            for x in json:
                idd = x["id"]
                table = x["table"]
                client = x["client"]
                state = x["state"]
                waiter = x["waiter"]
                price = x["price"]
                lines = x["lines"]
                newOrder = Order(idd,table,client,state,waiter,price,lines)

        return newOrder

    #Return a list of orders
    def getOrders(self):
        url = "http://localhost:8069/restaurapp_app/getOrders"
        response = requests.request("GET", url)
        if response.status_code == 200:
            data = response.json()
        else:
            print("Error GET")
            return None

        json = {}
        listOrders = {}
        json = data["data"]
        
        for x in json:
            idd = x["id"]
            table = x["table"]
            client = x["client"]
            state = x["state"]
            waiter = x["waiter"]
            price = x["price"]
            lines = x["lines"]
            newOrder = Order(idd,table,client,state,waiter,price,lines)
            listOrders[idd] = newOrder

        return listOrders

    def addOrder(self,order):
        url = "http://localhost:8069/restaurapp_app/addOrder"
        params = {
            "table":order.getTable(),
            "client":order.getClient(),
            "state":order.getState(),
            "waiter":order.getWaiter(),
            "price":order.getPrice(),
            "lines":order.getLines()
        }
        response = requests.post(url=url,json=params)
        if (response.status_code == 201):
            jsonReturned = r.json()
            if (len(jsonReturned) > 0):
                jsonId = jsonReturned['result']['id']
                order.setId(jsonId)
                return True
            else:
                print("Error posting!")
                return False
        else:
            print("*Error posting*")
            return False

    def updateOrder(self,order):
        url = "http://localhost:8069/restaurapp_app/updateOrder"
        params = {
            "id":order.getId(),
            "table":order.getTable(),
            "client":order.getClient(),
            "state":order.getState(),
            "waiter":order.getWaiter(),
            "price":order.getPrice(),
            "lines":order.getLines()
        }
        response = requests.put(url=url,json=params)
        if (response.status_code == 200):
            return True
        else:
            return False

    def deleteOrder(self,id):
        url = "http://localhost:8069/restaurapp_app/delOrder"
        params = {
            "id":id
        }
        response = requests.delete(url=url,json=params)
        if (response.status_code == 200):
            return True
        else:
            return False

                                    # ORDER LINE #

    def getLineById(self,id):
        url = "http://localhost:8069/restaurapp_app/getLine/"+str(id)
        response = requests.request("GET", url)
        if response.status_code == 200:
            data = response.json()
        else:
            print("Error GET")
            return None

        json = {}
        json = data["data"]
        if(len(json) == 0):
            return None
        else:
            for x in json:
                idd = x["id"]
                orderId = x["order_id"][0]
                productId = x["product_id"][0]
                quantity = x["quantity"] 
                fullName = x["fullName"]
                observations = x["observations"]
                newLine = Line(idd,orderId,productId,quantity,fullName,observations)

        return newLine

    #GET ALL LINES
    def getLines(self):
        url = "http://localhost:8069/restaurapp_app/getLines"
        response = requests.request("GET", url)
        if response.status_code == 200:
            data = response.json()
        else:
            print("Error GET")
            return None

        json = {}
        listLines = {}
        json = data["data"]
        
        for x in json:
            idd = x["id"]
            orderId = x["order_id"][0]
            productId = x["product_id"][0]
            quantity = x["quantity"]
            fullName = x["fullName"]
            observations = x["observations"]
            newLine = Line(idd,orderId,productId,quantity,fullName,observations)
            listLines[idd] = newLine

        return listLines

    def addLine(self,line):
        url = "http://localhost:8069/restaurapp_app/addLine"
        params = {
            "order_id":line.getOrderId(),
            "product_id":line.getProductId(),
            "quantity":line.getQuantity(),
            "observations":line.getObservations()
        }
        r = requests.post(url=url,json=params)
        if (r.status_code == 200):
            jsonReturned = r.json()
            if (len(jsonReturned) > 0):
                jsonId = jsonReturned['result']['id']
                line.setId(jsonId)
                return True
            else:
                print("Error posting")
                return False
        else:
            print("Error posting")
            return False

    def updateLine(self,line):
        url = "http://localhost:8069/restaurapp_app/updateLine"
        params = {
            "id":line.getId(),
            "order_id":line.getOrderId(),
            "product_id":line.getProductId(),
            "quantity":line.getQuantity(),
            "observations":line.getObservations()
        }
        r = requests.put(url=url,json=params)
        if (r.status_code == 200):
            jsonreturned = r.json()
            newFullName = jsonreturned['result']['full_name']
            line.setFullName(newFullName)
            return True
        else:
            return False

    def deleteLine(self,id):
        url = "http://localhost:8069/restaurapp_app/deleteLine"
        params = {
            "id":id
        }
        r = requests.delete(url=url,json=params)
        if (r.status_code == 200):
            return True
        else:
            return False

                                                #Confirm Order#

    def confirmOrder(self,order):
        url = "http://localhost:8069/restaurapp_app/confirmOrder/"+str(order.getId())
        response = requests.request("GET",url)
        if response.status_code == 200:
            data = response.json()
        else:
            print("ERROR CONFIRMING")
            return None

        state = data['stateOrder']
        order.setState(state)
        return True