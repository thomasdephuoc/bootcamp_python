import getopt, sys, argparse

'''
dict = {'Cake' : 'yummy'}
for key, value in dict.items() :
    print (key, value) 
'''

recipes = {'sandwich' : {'ingredients': 'ham, bread, cheese, tomatoes', 'meal' : 'lunch', 'prep_time' : '10'},
'cake' : {'ingredients': 'flour, sugar, eggs', 'meal' : 'dessert', 'prep_time' : '60'}, 
'salad' : {'ingredients': 'avocado, arugula, tomatoes, spinach', 'meal' : 'lunch', 'prep_time' : '15' }}

def print_recipe(recipe_name):
    print(f'Recipe for {recipe_name}:\nIngredients list: {recipes[recipe_name]["ingredients"]}\nTo be eated for {recipes[recipe_name]["meal"]}.\nTakes {recipes[recipe_name]["prep_time"]} minutes of cooking.')

def del_recipe(recipe_name):
    del recipes[recipe_name]

def add_recipe(recipe_name, ingredients, meal, prep_time):
    recipes[recipe_name] = {'ingredients': ingredients, 'meal' : meal, 'prep_time' : prep_time}

def print_cookbook():
    for recipe_name, content in recipes.items():
         print(recipe_name)

parser = argparse.ArgumentParser("Please add your recipe name, ingredients, meal type and preparation time")
parser.add_argument('recipe_name')
parser.add_argument('ingredients')
parser.add_argument('meal_type')
parser.add_argument('preparation_time')

user_input = 0
while user_input != 5:
    user_input = int(input("Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n"))
    if user_input == 1:
        recipe_input = parser.parse_args()
        add_recipe(recipe_input.recipe_name, recipe_input.ingredients, recipe_input.meal_type, recipe_input.preparation.time)
    elif user_input == 2:
        recipe_input = input("Please add your recipe name, ingredients, meal type and preparation time")
        add_recipe(recipe_input)
    elif user_input == 3:
        recipe_input = input("Please enter the recipe's name to get its details:")
        print_recipe(recipe_input)
    elif user_input == 4:
        print_cookbook()
    elif user_input == 5:
        print("Cookbook closed.")
    else:
        user_input = int(input("This option does not exist, please type the corresponding number.\nTo exit, enter 5."))
    print("\n")


