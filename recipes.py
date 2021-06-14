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

add_recipe()