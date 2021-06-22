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
    print('Recipe successfully added for ' + name + ': ')

    #Write each item in the recipe.
    count = len(ingredient_list)
    for item in ingredient_list:
        recipes.write(item)
        recipes.write('\n')
        print(item)
    
    recipes.close()

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

    return(recipe_dic)

    recipes.close()

def create_menu():

    menu_string = input('What are you going to make this week? ')
    menu_list = menu_string.split(', ')
    item_string = ''
    recipes_dic = get_recipes()

    for dish in menu_list:
        ingredient_list = (recipes_dic[dish])
        for item in ingredient_list:
            ingredient_string = item[0] + ', ' + item[1]
            shopping_list.append(ingredient_string)

    print()
    print("To make "+ menu_string + " you'll need:")

    for item in shopping_list:
        print(item)
        
def main():

    selection = input('''
    1. Add Recipes
    2. View Recipes
    3. Create the week's menu!
    
    ''')

    if selection == "1":
        add_recipe()
    elif selection == '2':
        view_recipes()
    elif selection == '3':
        create_menu()

shopping_list = []
main()