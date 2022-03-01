# JSON Database
from tinydb import TinyDB

class dbHandler:
    def __init__(self):
        self.ingredientDB = TinyDB("backend/db/foodcomposition.json")
        self.recipeDB = TinyDB("backend/db/recipes.json")
        self.wRecipes = self.recipeDB.table('web_recipes')
        self.uRecipes = self.recipeDB.table('user_recipes')


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