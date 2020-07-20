import getopt, random, sys

def is_list_of_strings(lst):
        if lst and isinstance(lst, list):
            return all(isinstance(elem, str) for elem in lst)
        else:
            return False

class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients, 
        self.description = description
        self.recipe_type = recipe_type
        exit = 0
        if isinstance(name,str) == False or len(name) == 0:
            print("Name missing")
            exit = 1
        if isinstance(cooking_lvl,int) == False or cooking_lvl < 1 or cooking_lvl > 5:
            print("Cooking level needs to be between 1 and 5")
            exit = 1
        if isinstance(cooking_time,int) == False or cooking_time < 0:
            print("Cooking time needs to be positive or nul")
            exit = 1
        if is_list_of_strings(ingredients) == False:
            print("Ingredients need to be a list of ingredients") 
            exit = 1   
        if isinstance(recipe_type,str) == False or (recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert"):
            print("Recipe should be either starter, lunch or dessert")
            exit = 1
        if exit == 1:
            sys.exit()

    def __str__(self):
        return 'Name: {self.name}\nCooking level:{self.cooking_lvl}\nCooking time: {self.cooking_time}\nIngredients: {self.ingredients}\nDescription: {self.description}\nRecipe type: {self.recipe_type}\n'.format(self=self)
        