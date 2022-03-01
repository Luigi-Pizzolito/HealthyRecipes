# JSON Database
from tinydb import TinyDB, Query
class dbHandler:
    def __init__(self):
        self.ingredientDB = TinyDB("backend/db/foodcomposition.json")
        self.fetchedQueries = self.ingredientDB.table('fetched_queries')
        self.ingredients = self.ingredientDB.table('ingredients')

        self.recipeDB = TinyDB("backend/db/recipes.json")
        self.wRecipes = self.recipeDB.table('web_recipes')
        self.uRecipes = self.recipeDB.table('user_recipes')


    # DB actions for ingredients
    def addIngredients(self, ingredients):
        self.ingredients.insert_multiple(ingredients)
    def addFetchedQuery(self, query):
        if self.getFetchedQuery(query):
            self.fetchedQueries.insert({"searched": query})

    def getFetchedQuery(self, query):
        field = Query()
        return not self.fetchedQueries.contains(field.searched == query)

    # def removeIngredientByURL(url):
    #     pass

    def queryIngredientsByName(self, name, max_results=1000000, include_alias=True):
        test_contains = lambda value, search: search in value
        field = Query()
        return self.ingredients.search(field.name.test(test_contains, name))[:max_results]

    def queryIngredientsByInfo(self, info, max_results, include_alias=True):
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