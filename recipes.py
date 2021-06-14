def add_recipe():
    
    again = 'y'
    recipe_dic = {}

    name = input("Enter recipe name: ")

    while again == 'y':
        item = input("Enter item: ")
        amount = input("Enter amount: ")
        recipe_dic[item] = amount

        again = input("Would you like to add another item? (y/n) ")

    print(recipe_dic)

def get_recipes():

##We have to make sure to create a file if there is none. 

    recipes = open('recipes.txt','r')

    print(recipes.read())

def menu():

    selection = input('''
    1. Add Recipes
    2. View Recipes
    
    ''')
    if selection == "1":
        add_recipe()
    else:
        get_recipes()


menu()