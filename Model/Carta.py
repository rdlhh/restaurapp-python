import ControlCat, ControlIngredients, ControlProduct, ControlOrder, ControlInvoice
from Order import Order
from orderLine import Line

controllerCAT = ControlCat.ControlCat()
controllerINGRE = ControlIngredients.ControlIngredients()
controllerPROD = ControlProduct.ControlProduct()
controllerORDER = ControlOrder.ControlOrder()
controllerINVOICE = ControlInvoice.ControlInvoice()

choice = 0
while choice != 5:
    print("1-CRUD Categories")
    print("2-CRUD Products")
    print("3-CRUD Ingredients")
    print("4-CRUD Order")
    print("5-Confirm Invoice")
    print("6-Exit")

    choice = int(input("Select: "))

    if choice == 1:
        choiceCat = 0
        cat = controllerCAT.chargeCategories()
        while choiceCat != 4:
            print("1-Create a category")
            print("2-Update a category")
            print("3-Delete a category")
            print("4-Exit")
            choiceCat = int(input("Select: "))
            if choiceCat == 1:
                name = input("Name of the category: ")
                jason = {
                    "name": name
                }
                result = controllerCAT.createCategory(jason)
                if result == True:
                    print("Category added")
                else:
                    print(result)

            if choiceCat == 2:
                for category in cat:
                    print("ID:",category, " - Name:", cat[category].getName())
                idcat = int(input("Select the category you want to update: "))
                upCatChoice = 0
                name= ""
                while upCatChoice != 3:
                    print("1-Change the name")
                    print("2-Exit")

                    upCatChoice = int(input("Select: "))
                    if upCatChoice == 1:
                        name = input("New name: ")
                    if upCatChoice == 2:
                        break

                jason = {}
                jason["id"]=idcat
                if name !="":
                    jason["name"] = name
                result = controllerCAT.updateCategory(jason)
                if result ==True:
                    print("Category updated")
                else:
                    print(result)

            if choiceCat == 3:
                for category in cat:
                    print("ID:",category, " - Name:", cat[category].getName())
                idcat = int(input("Select the category you want to delete: "))
                jason = {
                    "id": idcat
                }
                result = controllerCAT.deleteCategory(jason)
                if result ==True:
                    print("Category deleted")
                else:
                    print(result)

    if choice == 2:
        choiceProd = 0
        prod = controllerPROD.getAllProducts()
        while choiceProd != 4:
            print("1-Create a product")
            print("2-Update a product")
            print("3-Delete a product")
            print("4-Exit")
            choiceProd = int(input("Select: "))
            if choiceProd == 1:
                name = input("Name of the product: ")
                desc = input("Description of the product: ")
                price = float(input("Price of the product: "))
                cat = controllerCAT.chargeCategories()
                for category in cat:
                    print("ID:",category, " - Name:", cat[category].getName())
                idcat = int(input("Select the category for the product: "))
                ingre = controllerINGRE.chargeIngredients()
                ingres = []
                idingre = -1
                while idingre !=0:
                    for ingredient in ingre:
                        print("ID:",ingredient, " - Name:", ingre[ingredient].getName())
                    print("Press 0 to exit")
                    idingre = int(input("Select the ingredients of the product: "))
                    if idingre ==0:break
                    ingres.append(idingre)
                jason = {
                    "name": name,
                    "description": desc,
                    "price":price,
                    "category":category,
                    "ingredients":ingres
                }
                result = controllerPROD.createProduct(jason)
                if result == True:
                    print("Product added")
                else:
                    print(result)

            if choiceProd == 2:
                for product in prod:
                    print("ID:",product, " - Name:", prod[product].getName(), " - Price:", prod[product].getPrice())
                idprod = int(input("Select the product you want to update: "))
                upProdChoice = 0
                name=""
                desc = ""
                price=0
                category=0
                ingredients=[]
                while upProdChoice != 7:
                    print("1-Change the name")
                    print("2-Change the description")
                    print("3-Change the price")
                    print("4-Change the category")
                    print("5-Change the ingredients")
                    print("6-Finish editing")
                    upProdChoice = int(input("Select: "))
                    if upProdChoice == 1:
                        name = input("New name: ")
                    if upProdChoice == 2:
                        desc = input("New desc: ")
                    if upProdChoice == 3:
                        price = float(input("New price: "))
                    if upProdChoice == 4:
                        cat = controllerCAT.chargeCategories()
                        for category in cat:
                            print("ID:",category, " - Name:", cat[category].getName())
                        category = int(input("New category: "))
                    if upProdChoice == 5:
                        ingre = controllerINGRE.chargeIngredients()
                        idingre = -1
                        while idingre !=0:
                            for ingredient in ingre:
                                print("ID:",ingredient, " - Name:", ingre[ingredient].getName())
                            print("Press 0 to exit")
                            idingre = int(input("Select the ingredients of the product: "))
                            if idingre ==0:break
                            ingredients.append(idingre)
                    if upProdChoice == 6:
                        break

                jason = {}
                jason["id"]=idprod
                if name !="":
                    jason["name"] = name
                if desc !="":
                    jason["description"] = desc
                if price>0:
                    jason["price"] = price
                if category>0:
                    jason["category"] = category
                if len(ingredients) >0:
                    jason["ingredients"]=ingredients
                result = controllerPROD.updateProduct(jason)
                if result ==True:
                    print("Product updated")
                else:
                    print(result)

            if choiceProd == 3:
                for product in prod:
                    print("ID:",product, " - Name:", prod[product].getName(), " - Price:", prod[product].getPrice())
                idprod = int(input("Select the product you want to delete: "))
                jason = {
                    "id": idprod
                }
                result = controllerPROD.deleteProduct(jason)
                if result ==True:
                    print("Product deleted")
                else:
                    print(result)

    if choice == 3:
        choiceIngre = 0
        ingre = controllerINGRE.chargeIngredients()
        while choiceIngre != 4:
            print("1-Create an ingredient")
            print("2-Update an ingredient")
            print("3-Delete an ingredient")
            print("4-Exit")
            choiceIngre = int(input("Select: "))
            if choiceIngre == 1:
                name = input("Name of the ingredient: ")
                obs = input("Any description?" )
                jason = {
                    "name": name,
                }
                if len(obs) >0 or obs != None:
                    jason["description"] = obs
                result = controllerINGRE.createIngredient(jason)
                if result == True:
                    print("Ingredient added")
                else:
                    print(result)

            if choiceIngre == 2:
                for ingredient in ingre:
                    print("ID:",ingredient, " - Name:", ingre[ingredient].getName())
                idingre = int(input("Select the ingredient you want to update: "))
                upIngreChoice = 0
                observations=""
                name=""
                while upIngreChoice != 4:
                    print("1-Change the name")
                    print("2-Change the observations")
                    print("3-Exit")

                    upIngreChoice = int(input("Select: "))
                    if upIngreChoice == 1:
                        name = input("New name: ")
                    if upIngreChoice == 2:
                        observations = input("New description: ")
                    if upIngreChoice == 3:
                        break

                jason = {}
                jason["id"]=idingre
                if name !="":
                    jason["name"] = name
                if observations != "":
                    jason["observations"] = observations
                result = controllerINGRE.updateIngredient(jason)
                if result ==True:
                    print("Ingredient updated")
                else:
                    print(result)

            if choiceIngre == 3:
                for ingredient in ingre:
                    print("ID:",ingredient, " - Name:", ingre[ingredient].getName())
                idingre = int(input("Select the ingredient you want to delete: "))
                jason = {
                    "id": idingre
                }
                result = controllerINGRE.deleteIngredient(jason)
                if result ==True:
                    print("Ingredient deleted")
                else:
                    print(result)
            
            if choiceIngre == 4:
                break

    if choice == 4:
        choiceOrder = 0
        while choiceOrder != 7:
            print("1-Create a order")
            print("2-Read")
            print("3-Update a order")
            print("4-Delete")
            print("5-Confirm an order")
            print("6-Exit")
            choiceOrder = int(input("Select: "))
            if choiceOrder == 1:
                table = input("Number of table: ")
                client = input("Client: ")
                waiter = input("Waiter: ")
                newOrder = Order(None,table,client,'A',waiter,None,None)
                if controllerORDER.addOrder(newOrder):
                    print("\tNew order added with id ",newOrder.getId())
                else:
                    print("\tError. Not added")
                    break
                print("1) Add lines to this order")
                print("0) Exit and continue")
                opOC = int(input("What do you want to do now?: "))
                if opOC == 1:
                    while True:
                        prod = controllerPROD.getAllProducts()
                        print("1) Create new line")
                        print("0) Exit and continue")
                        opOCC = int(input("Select an option: "))
                        if opOCC == 0:
                            break
                        else:
                            #MIENTRAS EL USUARIO QUIERA, VAMOS CREANDO LINEAS PARA ESTA ORDEN
                            print("\nWe have the following products:")
                            for product in prod:
                                print("ID:",product, " - Name:", prod[product].getName())
                            productId = int(input("Enter the product to add to this line: "))
                            quantity = int(input("Enter the quantity for this product: "))
                            observations = input("Observations: ")
                            newLine = Line(None,newOrder.getId(),productId,quantity,None,observations)
                            if controllerORDER.addLine(newLine):
                                print("New line added!")
                            else:
                                print("Error! Not added")

            if choiceOrder == 2:
                while(True):
                            print("1- Read one order by ID")
                            print("2- Read all orders")
                            print("0- Exit")
                            opRead = int(input("Choose an option:"))
                            ord = controllerORDER.getOrders()
                            for order in ord:
                                print("\tID ",order)
                            if opRead == 1:
                                idd = input("Enter the order ID:")
                                order = controllerORDER.getOrderById(idd)
                                if order == None:
                                    print("\tTHIS ORDER DOESN'T EXISTS")
                                    break
                                lines = order.getLines()
                                messsage = ""
                                if len(lines) <= 0:
                                    message = "\tID - "+str(order.getId())+"\n\tTable: "+str(order.getTable())+"\n\tClient: "+str(order.getClient())+"\n\State: "+str(order.getState())+"\n\tWaiter: "+str(order.getWaiter())+"\n\tPrice €: "+str(order.getPrice())+"\n\tNo lines"
                                    print(message)
                                    print()
                                else:
                                    message = "\tID - "+str(order.getId())+"\n\tTable: "+str(order.getTable())+"\n\tClient: "+str(order.getClient())+"\n\State: "+str(order.getState())+"\n\tWaiter: "+str(order.getWaiter())+"\n\tPrice €: "+str(order.getPrice())+"\n\tLines:\n\t\t"
                                    for l in lines:
                                        message += str(controllerORDER.getLineById(l).getFullName())
                                    print(message)
                                    print()

                            elif opRead == 2:
                                ord = controllerORDER.getOrders()
                                for order in ord:
                                    print("\tID ", order," - Table: ",ord[order].getTable(),", Price: ",ord[order].getPrice(),"€, State: ",ord[order].getState())

                            elif opRead == 0:
                                break

            if choiceOrder == 3:
                ord = controllerORDER.getOrders()
                for order in ord:
                    print("ID: ", order)
                idd = input("Enter the order to update (his ID):")
                order = controllerORDER.getOrderById(idd)
                if order == None:
                    print("\tThis order doesn't exists")
                else:
                    while(True):
                        print("What param do you want to update?:")
                        print("1- Table ",order.getTable())
                        print("2- Client ",order.getClient())
                        print("3- Waiter ",order.getWaiter())
                        print("4- Lines ",order.getLines())
                        print("5- Update the order")
                        print("0- Exit")
                        opParam = int(input("Choose a param: "))
                        if opParam == 1:
                            table = input("Enter the new table name: ")
                            order.setTable(table)
                        
                        elif opParam == 2:
                            client = input("Enter the new client: ")
                            order.setClient(client)

                        elif opParam == 3:
                            waiter = input("Enter the new waiter: ")
                            order.setWaiter(waiter)

                        elif opParam == 4:
                            print("We have the following lines:")
                            lines = controllerORDER.getOrderById(idd).getLines()
                            for lin in lines:
                                linea = controllerORDER.getLineById(lin)
                                pr = controllerPROD.findProduct(linea.getProductId())
                                print("\tID ",linea.getId()," - Name: ",pr.getName())
                            idL = int(input("Select a line to update: "))
                            lineU = controllerORDER.getLineById(idL)
                            p = controllerPROD.findProduct(lineU.getProductId())
                            while True:
                                print("What do u want to update?")
                                print("1) Product (",p.getName(),")")
                                print("2) Quantity (",lineU.getQuantity(),")")
                                print("3) Observations (",lineU.getObservations(),")")
                                print("0) Exit")
                                opOU = int(input("Select an option: "))
                                if opOU == 1:
                                    pro = controllerPROD.getAllProducts()
                                    for product in pro:
                                        print("ID:",product, " - Name:", pro[product].getName())
                                    idP = int(input("Enter the new product for this line: "))
                                    lineU.setProductId(idP)
                                elif opOU == 2:
                                    quantity = int(input("Enter a new quantity for the product: "))
                                    lineU.setQuantity(quantity)
                                elif opOU == 3:
                                    observations = input("Observations for this line: ")
                                    lineU.setObservations(observations)
                                elif opOU == 0:
                                    controllerORDER.updateLine(lineU)
                                    print("Line modified")
                                    break

                        elif opParam == 5:
                            if controllerORDER.updateOrder(order):
                                print("\tOrder updated")
                                break
                            else:
                                print("\tERROR. Not updated")

                        elif opParam == 0:
                            break

            if choiceOrder == 4:
                while True:
                    print("1) Delete an order")
                    print("0) Exit")
                    opOD = int(input("Select an option: "))
                    if opOD == 0:
                        break
                    elif opOD == 1:
                        o = controllerORDER.getOrders()
                        for order in o:
                            print("ID: ", order)
                        idd = input("Enter the order ID to remove:")
                        orderD = controllerORDER.getOrderById(idd)
                        if orderD == None:
                            print("\tError. This order doesn't exists")
                        else:
                            if controllerORDER.deleteOrder(idd):
                                print("\tOrder removed")
                            else:
                                print("\tERROR. Not removed")

            if choiceOrder == 5:
                o = controllerORDER.getOrders()
                for order in o:
                    print("ID: ", order)
                idd = input("Enter the order (his ID):")
                order = controllerORDER.getOrderById(idd)
                if order == None:
                    print("\tThis order doesn't exists")
                else:
                    if order.getState() == 'A':
                        print("Order state: ",order.getState())
                        confirm = int(input("CONFIRM ORDER? (1-YES | 0-NO) "))
                        if confirm == 1:
                            if controllerORDER.confirmOrder(idd):
                                print("Order confirmed (State: ",order.getState(),")")
                            else:
                                print("Error. Not confirmed")
                        elif confirm == 0:
                            break

                    else:
                        print("ERROR! The order is already confirmed")
                    
            if choiceOrder == 6:
                break

    if choice == 5:
        inv = controllerINVOICE.getInvoices()
        for invoice in inv:
            print("\t ID: ",invoice," - Ref: ",inv[invoice].getRef(),", Date: ",inv[invoice].getDate(),", Total: ",inv[invoice].getTotal(),"€, Client: ",inv[invoice].getClient())
        id = input("Wich order do you want to continue? ")
        invoice = controllerINVOICE.getInvoiceById(id)
        if invoice == None:
            print("This invoice doesn't exists")
        else:
            if invoice.getState() == 'D':
                if controllerINVOICE.confirmInvoice(id):
                    print("Invoice confirmed!")
                    break
                else:
                    print("Error. Invoice not confirmed")
            else:
                print("Error!")
                break

    if choice == 6:
        print("Thanks for using RestaurApp! :)")
        break