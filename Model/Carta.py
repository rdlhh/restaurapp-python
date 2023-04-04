import ControlCat, ControlIngredients, ControlProduct, ControlOrder
from Order import Order
from orderLine import Line

controllerCAT = ControlCat.ControlCat()
controllerINGRE = ControlIngredients.ControlIngredients()
controllerPROD = ControlProduct.ControlProduct()
controllerORDER = ControlOrder.ControlOrder()

choice = 0
while choice != 5:
    print("1-CRUD Categories")
    print("2-CRUD Products")
    print("3-CRUD Ingredients")
    print("4-CRUD Order")
    print("5-Exit")

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
                        print("1) Create new line")
                        print("0) Exit and continue")
                        opOCC = int(input("Select an option: "))
                        if opOCC == 0:
                            break
                        else:
                            #MIENTRAS EL USUARIO QUIERA, VAMOS CREANDO LINEAS PARA ESTA ORDEN
                            print("\nWe have the following products:")
                            for product in prod:
                                print("ID:",product, " - Name:", prod[product].getName(), " - Price:", prod[product].getPrice())
                            productId = int(input("Enter the product to add to this line: "))
                            quantity = int(input("Enter the quantity for this product: "))
                            observations = input("Observations: ")
                            newLine = Line(None,newOrder.getId(),productId,quantity,None,observations)
                            if controllerORDER.addLine(newLine):
                                print("New line added with ID: ",newLine.getId())
                            else:
                                print("Error. Not added")

            if choiceOrder == 2:
                for table in tables:
                    if tables[table].getState() != "F":
                        print("ID:",table, " - Num:", tables[table].getTableNum(), " - Diners:", tables[table].getDiners(), " - Waiter:", tables[table].getWaiter(), " - State:", tables[table].getState())
                idTable = int(input("Select the order you want to update: "))
                upTableChoice = 0
                num = 0
                diners = 0
                waiter = ""
                client = ""
                state = ""
                while upTableChoice != 6:
                    print("1-Change the num")
                    print("2-Change the number of diners")
                    print("3-Change the waiter")
                    print("4-Change the client")
                    print("5-Change the state(W:Waiting/E:Eating)")
                    print("6-Exit")
                    upTableChoice = int(input("Select: "))
                    if upTableChoice == 1:
                        num = int(input("New num: "))
                    if upTableChoice == 2:
                        diners = int(input("Number of diners: "))
                    if upTableChoice == 3:
                        waiter = input("New waiter: ")
                    if upTableChoice == 4:
                        client = input("New client name: ")
                    if upTableChoice == 5:
                        state = input("New state(W:Waiting/E:Eating): ")

                jason = {}
                jason["id"]=idTable
                if num !=0:
                    jason["num"] = num
                if diners != 0:
                    jason["diners"]=diners
                if waiter != "":
                    jason["waiter"]=waiter
                if client !="":
                    jason["client"] = client
                if state =="W":
                    jason["state"] = state
                if state =="E":
                    jason["state"] = state
                if state != "W" and state != "E":
                    print("The state value is not correct, no changes made in the state")
                result = controllerORDER.updateTable(jason)
                if result ==True:
                    print("Table updated")
                else:
                    print(result)

            if choiceOrder == 3:
                for table in tables:
                    if tables[table].getState() != "F":
                        print("ID:",table, " - Num:", tables[table].getNum(), " - Diners:", tables[table].getDiners(), " - Waiter:", tables[table].getWaiter(), " - State:", tables[table].getState())
                idTable = int(input("Select the order you want to update: "))
                jason = {
                    "id": idTable,
                    "state":"F"
                }
                result = controllerORDER.finishTable(jason)
                if result ==True:
                    print("Order finished")
                else:
                    print(result)

            if choiceOrder == 4:
                for table in tables:
                    if tables[table].getState() != "F":
                        print("ID:",table, " - Num:", tables[table].getNum(), " - Diners:", tables[table].getDiners(), " - Waiter:", tables[table].getWaiter(), " - State:", tables[table].getState(), " - Total:", tables[table].getTotal())
                        if len(tables[table].getOrder())>0:
                            for order in tables[table].getOrder():
                                print("\t",tables[table].getOrder()[order].getQuant()," - ",tables[table].getOrder()[order].getProduct().getName()," - ",tables[table].getOrder()[order].getPrice())
                        else:
                            print("Not ordered nothing")

            if choiceOrder == 5:
                for table in tables:
                    if tables[table].getState() != "F":
                        print("ID:",table, " - Num:", tables[table].getNum(), " - Diners:", tables[table].getDiners(), " - Waiter:", tables[table].getWaiter(), " - State:", tables[table].getState(), " - Total:", tables[table].getTotal())
                        if len(tables[table].getOrder())>0:
                            for order in tables[table].getOrder():
                                print("\t",tables[table].getOrder()[order].getQuant()," - ",tables[table].getOrder()[order].getProduct().getName()," - ",tables[table].getOrder()[order].getPrice())
                        else:
                            print("Not ordered anything")
                idTable = int(input("Select the order: "))
                
                filterCat = 0
                cat = controllerCAT.chargeCategories()
                while filterCat != (len(cat)+1):
                    for category in cat:
                        print(category," - ",cat[category].getName())
                    print((len(cat)+1),"-Exit")
                    filterCat = int(input("Select the category: "))
                    if filterCat == (len(cat)+1): break

                    prod = controllerPROD.getAllProducts()
                    for product in prod:
                        if prod[product].getCategory().getName() ==controllerCAT.findCategory(filterCat).getName():
                            print(product," - ",prod[product].getName()," - ",prod[product].getPrice())

                    idProd = int(input("Select the plate: "))
                    quant = int(input("How many plates: "))
                    jason = {
                        "numTable":idTable,
                        "quant":quant,
                        "product":idProd
                    }

                    result = controllerORDER.addOrder(jason)
                    if result ==True:
                        print("Order added")
                    else:
                        print(result)
                    
            if choiceOrder == 6:
                break

    if choice == 5:
        print("Thanks for using RestaurApp! :)")
        break