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

    recipe_dic = {}
    inner_dic = {}
    item_dic = {}
    count = 0
    recipe_name = ''

    for line in recipes:
        if line.rstrip().isalpha() and not ',' in line:
            recipe_name = line.rstrip()
            print(recipe_name)
            count = count + 1
        elif ',' in line:
            item_list = line.split(', ')
            item_dic[item_list[0]] = item_list[1].rstrip()
        elif line == '\n':
            recipe_dic[recipe_name] = item_dic
            item_dic = {}

    recipe_dic[recipe_name] = item_dic

    print("We found " + str(count) + " recipes.")

    print(recipe_dic)

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