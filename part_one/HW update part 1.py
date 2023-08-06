with open('recipes.txt', encoding='utf-8') as file_work:
    cook_book = {}
    for line in file_work:
        dish_name = line.strip()
        counter = file_work.readline()
        list_of_ingredient = []
        for i in range(0, int(counter)):
            temp_dict = {}
            ingredient = file_work.readline().strip().split('|')
            temp_dict['ingredient_name'] = ingredient[0]
            temp_dict['quantity'] = ingredient[1]
            temp_dict['measure'] = ingredient[2]
            list_of_ingredient.append(temp_dict)
        cook_book[dish_name] = list_of_ingredient
        file_work.readline()
print(cook_book)