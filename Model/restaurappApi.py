import json
import requests
from category import Category
from product import Product
from ingredients import Ingredients

def getCategories():
        url = "http://localhost:8069/restaurapp_app/category"

        querystring = {""}

        headers = {
        }
        responseC = requests.request("GET",url)
        if responseC.status_code == 200:
            dataC = responseC.json()
            categories = {} # Key -> Id, Value --> Category
            for c in range(len(dataC["data"])) :   
                categoryId = dataC["data"][c]["id"]
                categoryName = dataC["data"][c]["name"]
                categoryProducts ={}
                for cat in range(len(dataC["data"][c]["product"])):
                    product = dataC["data"][c]["product"][cat]
                    categoryProducts[product]= product
                newCategory = Category(categoryId,categoryName,categoryProducts)
                categories[categoryId] = newCategory
        return categories

def getIngredients():
        url = "http://localhost:8069/restaurapp_app/ingredient"

        querystring = {""}

        headers = {
        }
        responseI = requests.request("GET",url)
        if responseI.status_code == 200:
            dataI = responseI.json()
            ingredients = {} # Key -> Id, Value --> Ingredient
            for i in range(len(dataI["data"])) :    
                ingredientId = dataI["data"][i]["id"]
                ingredientName = dataI["data"][i]["name"]
                ingredientObservation = dataI["data"][i]["observation"]
                ingredientProducts = {}
                for cat in range(len(dataI["data"][i]["products"])):
                    product = dataI["data"][i]["products"][cat]
                    ingredientProducts[product]= product
                newIngredient = Ingredients(ingredientId,ingredientName,ingredientObservation,ingredientProducts)
                ingredients[ingredientId] = newIngredient
        return ingredients

def getProducts():
        url = "http://localhost:8069/restaurapp_app/products"

        querystring = {""}

        headers = {
        }
        responseP = requests.request("GET",url)
        if responseP.status_code == 200:
            dataP = responseP.json()
            products = {} # Key -> Id, Value --> Product
            for p in range(len(dataP["data"])) :    
                productId = dataP["data"][p]["id"]
                productName = dataP["data"][p]["name"]
                productDescription = dataP["data"][p]["description"]
                productPrice = dataP["data"][p]["price"]
                catID = dataP["data"][p]["category"][0]
                catName = dataP["data"][p]["category"][1]
                productCategory = Category(catID,catName,"null","null")
                productIngredients={}
                for nIng in range(len(dataP["data"][p]["ingredients"])):
                     Pingred= dataP["data"][p]["ingredients"][nIng]
                     productIngredients[Pingred]=Pingred
                newProduct = Product(productId,productName,productDescription,productCategory,productIngredients,productPrice)
                products[productId] = newProduct
                
        return products
