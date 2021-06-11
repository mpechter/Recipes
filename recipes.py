def get_recipe():
    
    again = 'y'
    recipe_dic = {}

    name = input("Enter recipe name: ")

    while again == 'y':
        item = input("Enter item: ")
        amount = input("Enter amount: ")
        recipe_dic[item] = amount

        again = input("Would you like to add another item? (y/n) ")

    return recipe_dic

def main():
    init = 'y'
    list_of_recipes = []
    
    while init == 'y':
        list_of_recipes.append(get_recipe())
        init = input("Would you like to enter a recipe? (y/n) ")

    print(list_of_recipes)

main()