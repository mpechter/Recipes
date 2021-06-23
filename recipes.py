def isName(line):
    if '\n' in line.rstrip():
        return False
    if ', ' in line:
        return False
    if len(line.rstrip()) == 0:
        return False
    return True

def get_recipes():
    try:
        recipes = open('recipes.txt','r')
    except:
        recipes = open('recipes.txt','a')
        print("No recipes entered; New file created.")
        return
    recipe_dic = {}
    ingredient_list = []
    count = 0
    recipe_name = ''

    for line in recipes:
        #In our format, if the line has letters but no commas, it is a recipe name. 
        if line.rstrip().isalpha() and not ',' in line:
            recipe_name = line.rstrip()
            count = count + 1
        #Any line with a comma is a line with an item and amount. 
        elif ',' in line:
            item_amount =line.rstrip().split(', ')
            ingredient_list.append(item_amount)

        #Thus when we reach a blank line, we know we've reached the end of a recipe. 
        elif line == '\n':
            recipe_dic[recipe_name] = ingredient_list
            #We need to reset this list so ingredients for the previous items aren't preserved. 
            ingredient_list = []

    recipe_dic[recipe_name] = ingredient_list
    recipes.close()
    return(recipe_dic)

def view_recipes():
    try:
        recipes = open('recipes.txt','r')
        recipe_list = []
        for line in recipes:
            if isName(line):
                recipe_name = line.rstrip()
                recipe_list.append(recipe_name)
        print('Recipes in the system are:')
        for recipe in recipe_list:
            print(recipe)
    except:
        recipes = open('recipes.txt','a')
        print("No recipes entered; New file created.")
    recipes.close()

    cont = input('\nClick any key to continue.')
    return

def add_recipe():

    ingredient_list = []
    item_amount = "_"
    name = input("Enter recipe name: ")

    while len(item_amount) > 0:
        item_amount = input("Enter item and amount, separated by a comma: ")
        ingredient_list.append(item_amount)

    try:
        recipes = open('recipes.txt','a')
    except:
        recipes = open('recipes.txt','a')
        print("No recipes entered; New file created.")

    #Write the recipe's title.
    recipes.write(name)
    recipes.write('\n')
    print('\nRecipe successfully added for ' + name + ': ')

    #Write each item in the recipe.
    count = len(ingredient_list)
    for item in ingredient_list:
        recipes.write(item)
        recipes.write('\n')
        print(item)
    
    recipes.close()

    cont = input('\nClick any key to continue.')
    return

def create_menu():

    menu_string = input('What are you going to make this week? ')
    if len(menu_string) == 0:
        return
    menu_list = menu_string.split(', ')
    item_string = ''
    recipes_dic = get_recipes()

    for dish in menu_list:
        ingredient_list = (recipes_dic[dish])
        for item in ingredient_list:
            ingredient_string = item[0] + ', ' + item[1]
            shopping_list.append(ingredient_string)
    #This next sequence just adds 'and' to the string before the final item. 
    last = menu_list[-1]
    last_remove = ', ' + last
    menu_string = menu_string.replace(last_remove, ' and ')
    menu_string = menu_string + last

    print("\nTo make "+ menu_string + " you'll need: \n")
    shopping_list.sort()
    for item in shopping_list:
        print(item)

    cont = input('\nClick any key to continue.')
        
def menu():

    selection = '_'
    while len(selection)>0:
        selection = input('''
MAIN MENU:
1. View Recipes
2. Add Recipes
3. Create the week's menu!
    
        ''')

        if selection == "1":
            view_recipes()
        elif selection == '2':
            add_recipe()
        elif selection == '3':
            create_menu()

shopping_list = []
menu_string = ''
menu()
