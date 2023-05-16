import requests, json
from Invoice import Invoice

class ControlInvoice:

    #Return a list of invoices
    def getInvoices(self):
        url = "http://localhost:8069/restaurapp_app/invoice"
        response = requests.request("GET", url)
        if response.status_code == 200:
            data = response.json()
        else:
            print("Error GET")
            return None
            
        json = {}
        listInvoices = {}
        json = data["data"]
        
        for x in json:
            idd = x["id"]
            ref = x["ref"]
            date = x["date"]
            base = x["base"]
            iva = x["iva"]
            total = x["total"]
            state = x["state"]
            lines = x["lines"]
            client = x["client"]
            newInvoice = Invoice(idd,ref,date,base,iva,total,state,lines,client)
            listInvoices[idd] = newInvoice

        return listInvoices

    def getInvoiceById(self,id):
        url = "http://localhost:8069/restaurapp_app/getInvoice/"+str(id)
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
                ref = x["ref"]
                date = x["date"]
                base = x["base"]
                iva = x["iva"]
                total = x["total"]
                state = x["state"]
                lines = x["lines"]
                client = x["client"]
                newInvoice = Invoice(idd,ref,date,base,iva,total,state,lines,client)

        return newInvoice

    def confirmInvoice(self,id):
        url = "http://localhost:8069/restaurapp_app/confirmInvoice/"+id
        
        response = requests.request("GET",url=url)
        
        if response.status_code == 200:
            return True
        else:
            print("ERROR CONFIRMING")
            return None