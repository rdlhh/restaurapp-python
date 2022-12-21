from restaurappApi import getCategories,getIngredients,getProducts
from Order import Order
from productOrder import productOrder

class Control():

    def __init__(self):
        self._categories = {} #Key -> Id / Value -> Category 
        self._products = {} #Key -> Id / Value -> Product
        self._ingredients = {} #Key -> Id / Value -> Ingredient
        self._Orders = {}
        self._earned=0

        for Cid,category in getCategories().items():
            self._categories[Cid]=category

        for Pid,product in getProducts().items():
            self._products[Pid]=product

        for Iid,ingredient in getIngredients().items():
            self._ingredients[Iid]=ingredient

        for Cid,category in self._categories.items():
            for Pid,product in self._products.items():
                if product.getCategory().getId()==Cid:
                    newcategory= category
                    newproduct=product
                    product.setCategory(newcategory)
                    category.addProducts(newproduct,Pid)

        for Pid,product in self._products.items():
            for pIngredient in product.getIngredients():
                for Iid,ingredient in self._ingredients.items():
                    IngredienteProducto = ingredient
                    ProductoIngrediente = product
                    if pIngredient == int(Iid):
                        product.setIngredient(Iid,IngredienteProducto)
                        ingredient.setProduct(Pid,ProductoIngrediente)
                    
                
            """for productId in self._products:
                self._products[productId]"""
    
    def listCategories(self):
        return self._categories

    def checkCategory(self, categoryId):
        """""
        if categoryId not in self._categories:
            return False
        else:
            return True
        """""
        for Cid,category in self._categories.items():
            if Cid==int(categoryId):
            
                return True
        return False

    def listProducts(self,Cid):
        productById ={}
        for pid,product in self._products.items():
            if product.getCategory().getId()==int(Cid):
                productById[pid]=product
        return productById

    def checkProduct(self,id):
        for pid,product in self._products.items():
            if pid==int(id):
                return True
        return False

    def checkOrder(self,table):
        for Oid,order in self._Orders.items():
            if Oid==table:
                return True
        return False
            

    def selectProduct(self,id):
        for pid,product in self._products.items():
            if pid==int(id):
                return product

    def addProductOrder(self,table,choice,quantity):
        idorder = str(table) +"."+str(choice)

        product=self.selectProduct(choice)

        value = product.getPrice()*int(quantity)

        newProductOrder = productOrder(idorder,product,quantity,value)
        for Oid,order in self._Orders.items():
            if Oid==table:
                order.addProductOrders(idorder,newProductOrder)
    

    def orderDone(self,table):
        for Oid,order in self._Orders.items():
            if Oid==table:
                doneOrder =order
        self._earned=self._earned + float(doneOrder.getCost())
        self._Orders.pop(table)
        
    def seeProfits(self):
        return self._earned


    def addOrder(self,table):
        newOrder =Order(table)
        self._Orders[table]=newOrder
        

    def listOrders(self):
        return self._Orders
