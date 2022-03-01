# Database
from tinydb import TinyDB

class dbHandler:
    def __init__(self):
        self._ingredientDB = TinyDB("backend/db/foodcomposition.json")
        self._recipeDB = TinyDB("backend/db/recipes.json")


    # DB actions for ingredients
    def addIngredients():
        pass

    def removeIngredients():
        pass

    def queryIngredientsByName():
        pass

    def queryIngredientsByInfo():
        pass


    # DB actions for recipes
    def addRecipes():
        pass

    def removeRecipes():
        pass

    def queryRecipesByName():
        pass

    def queryRecipesByInfo():
        pass