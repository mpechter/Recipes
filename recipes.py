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
    ingredients_list = []
    count = 0
    recipe_name = ''

    for line in recipes:
        #In our format, if the line has letters but no commas, it is a recipe name. 
        if line.rstrip().isalpha() and not ',' in line:
            recipe_name = line.rstrip()
            print(recipe_name)
            count = count + 1
        #Any line with a comma is a line with an item and amount. 
        elif ',' in line:
            item_amount = [line.rstrip()]
            ingredients_list.append(item_amount)

        #Thus when we reach a blank line, we know we've reached the end of a recipe. 
        elif line == '\n':
            recipe_dic[recipe_name] = ingredients_list
            #We need to reset this list so ingredients for the previous items aren't preserved. 
            ingredients_list = []

    recipe_dic[recipe_name] = ingredients_list

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