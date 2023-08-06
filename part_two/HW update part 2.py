def get_shop_list_by_dishes(dishes, person_count):
    ingredients_list = []
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

    dish_dict = {}
    for dish in dishes:
        for cook_book_dish in cook_book[dish]:
            dish_dict_local = {}
            quantity_for_all = int(cook_book_dish['quantity']) * int(person_count)
            dish_dict_local['measure'] = cook_book_dish['measure']
            dish_dict_local['quantity'] = quantity_for_all
            if cook_book_dish['ingredient_name'] in dish_dict:
                dish_dict[cook_book_dish['ingredient_name']]['quantity'] += dish_dict_local['quantity']
            else:
                dish_dict[cook_book_dish['ingredient_name']] = dish_dict_local
    print(dish_dict)


get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 4)