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

def view_recipes():

    try:
        recipes = open('recipes.txt','r')
        print(recipes.read())
    except:
        recipes = open('recipes.txt','a')
        print("No recipes entered; New file created.")

    recipes.close()

def get_recipes():
    try:
        recipes = open('recipes.txt','r')
    except:
        recipes = open('recipes.txt','a')
        print("No recipes entered; New file created.")

    recipe_list = []

    count = 0

    for line in recipes:
        if line.rstrip().isalpha() and not ',' in line:
            print(line.rstrip())
            count = count + 1

    print("We found " + str(count) + " recipes.")

    recipes.close()


def menu():

    selection = input('''
    1. Add Recipes
    2. View Recipes
    3. Get Recipes
    
    ''')

    if selection == "1":
        add_recipe()
    elif selection == '2':
        view_recipes()
    elif selection == '3':
        get_recipes()


menu()