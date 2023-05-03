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
                client = x["clients"]
                state = x["state"]
                waiter = x["waiter"]
                price = x["tPrice"]
                lines = x["orderLine"]
                newOrder = Order(idd,table,client,state,waiter,price,lines)

        return newOrder

    #Return a list of orders
    def getOrders(self):
        url = "http://localhost:8069/restaurapp_app/order"
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
            client = x["clients"]
            state = x["state"]
            waiter = x["waiter"]
            price = x["tPrice"]
            lines = x["orderLine"]
            newOrder = Order(idd,table,client,state,waiter,price,lines)
            listOrders[idd] = newOrder

        return listOrders

    def addOrder(self,order):
        url = "http://localhost:8069/restaurapp_app/addOrder"
        params = {
            "table":order.getTable(),
            "clients":order.getClient(),
            "state":order.getState(),
            "waiter":order.getWaiter(),
            "tPrice":order.getPrice(),
            "orderLine":order.getLines()
        }
        response = requests.post(url=url,json=params)
        if (response.status_code == 200):
            jsonReturned = response.json()
            if (len(jsonReturned) > 0):
                jsonId = jsonReturned['result']['id']
                order.setId(jsonId)
                return True
            else:
                print("Error posting!")
                return False
        else:
            print("Error!")
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
                observations = x["description"]
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

            observations = x["description"]
            newLine = Line(idd,orderId,productId,quantity,observations)
            listLines[idd] = newLine

        return listLines

    def addLine(self,line):
        url = "http://localhost:8069/restaurapp_app/addLine"
        params = {
            "order_id":line.getOrderId(),
            "product_id":line.getProductId(),
            "quantity":line.getQuantity(),
            "description":line.getObservations()
        }
        r = requests.post(url=url,json=params)
        if (r.status_code == 200):
            jsonReturned = r.json()
            if (len(jsonReturned) > 0):
                jsonId = jsonReturned['result']
                newFullName = jsonReturned['result']
                line.setId(jsonId)
                line.setFullName(newFullName)
                return True
            else:
                print("¡ERROR!")
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
            "description":line.getObservations()
        }
        r = requests.put(url=url,json=params)
        if (r.status_code == 200):
            jsonreturned = r.json()
            newFullName = jsonreturned['result']
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