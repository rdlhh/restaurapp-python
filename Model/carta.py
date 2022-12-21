from Control import Control
from datetime import datetime
controler = Control()

def listCategories():
    categories = controler.listCategories()
    for id,category in categories.items():
        print("\n")
        print("Name: ",category.getName())
        print("\t Category ID: ",category.getId())
        print("\t Description: ",category.getDescription())
        print("\n")

def listProducts(categoryId):
    if controler.checkCategory(categoryId):
        products = controler.listProducts(categoryId)
        for pid,product in products.items():
            print("\n")
            print("Name: ",product.getName())
            print("\t Product ID: ",pid)
            print("\t Description: ",product.getDescription())
            print("\t Ingredients:")
            ingredients = product.getIngredients()
            for Iid,i in  ingredients.items():
                print("\t\t Ingredient: ",i.getName())
            print("\t Price: ",product.getPrice())
            print("\n")
    else:
        print("The id doesn't belong to any category")

def addOrder():
    table = input("Enter the number of the table: ")

    choice = 1
    controler.addOrder(table)  
    while(choice!=0):
        choice = int(input("Enter the id of the product (Enter 0 to end): "))
        if controler.checkProduct(choice):
            if(choice!=0):
                quant = input("Enter the quantity of the product: ")
                if(int(quant)>0):
                    controler.addProductOrder(table,choice,quant)
                    
                else:
                    print("The quantity of the product has to be grater than 0")
        elif(choice==0):
            break
        else:
            print("Product not found. Try again.")

def ListOrders():
    orders = controler.listOrders()
    for id,order in orders.items():
        print("\n")
        print("Table: ",order.getTable())
        productOrders = order.getProductOrders()
        for Pid,productOrder in  productOrders.items():
            print("\t\t Product: ",productOrder.getProduct().getName()," - Quantity: ",productOrder.getQuantity())
        print("\t Cost: ",order.getCost(),"€")
        print("\n")
    
def markDone():
    table = input("Enter the table of the order: ")
    if controler.checkOrder(table):
        controler.orderDone(table)
        print("Order done")
    else:
        print("ERROR: Order not found")

def profits():
    profit = controler.seeProfits()
    print("Profit of today until now: ",profit,"€")

def finalProfit():
    profit = controler.seeProfits()
    print("Final profit: ",profit,"€")


while True:  
    print("\n")
    print("1.- List categories")
    print("2.- List products from a category")
    print("3.- Made an order")
    print("4.- List active orders")
    print("5.- Mark an order as done")
    print("6.- See the current profit of today")
    print("7.- Exit")
    option = int(input("Choose option: "))
    print("\n")
    if(option == 7):
        finalProfit()

        print("\n BYE")
        break

    elif (option == 1):
        listCategories()
        
    elif (option == 2):
        categoryId = input("Enter the id of the wanted category: ")
        listProducts(categoryId)
        
    elif (option == 3):
        addOrder()
        
        
    elif (option == 4):
        ListOrders()
        
    elif (option == 5):
        markDone()

    elif (option == 6):
        profits()

    else:
        print("Option error")