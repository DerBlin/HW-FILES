def get_shop_list_by_dishes(dishes, person_count):
    ingredients_list = []
    with open('recipes.txt', encoding='utf-8') as file:
        key = file.readline().strip()
        count_string = int(file.readline())
        for el in range(0, count_string):
            # print(el)
            prod = file.readline().strip().split('|')
            ingredients = {'ingredient_name': prod[0], 'quantity': prod[1], 'measure': prod[2]}
            # ingredients['ingredient_name'] = prod[0]
            # ingredients['quantity'] = prod[1]
            # ingredients['measure'] = prod[2]
            res = ingredients
            # print(res)
            ingredients_list.append(res)
            # print(ingredients)
            # print(ingredients_list)
        # print(ingredients_list)
        second_ingredients_list = []
        not_empty_string = file.readline()
        second_key = file.readline().strip()
        count_for_duck = int(file.readline())
        for el in range(0, count_for_duck):
            prod1 = file.readline().strip().split('|')
            ingredients_for_duck = {'ingredient_name': prod1[0], 'quantity': prod1[1], 'measure': prod1[2]}
            res2 = ingredients_for_duck
            second_ingredients_list.append(res2)
        # print(second_ingredients_list)
        third_ingredients_list = []
        not_empty_string_2 = file.readline()
        third_key = file.readline().strip()
        count_potato = int(file.readline())
        for el in range(0, count_potato):
            prod2 = file.readline().strip().split('|')
            ingredients_for_potato = {'ingredient_name': prod2[0], 'quantity': prod2[1], 'measure': prod2[2]}
            res3 = ingredients_for_potato
            third_ingredients_list.append(res3)
        # print(third_ingredients_list)
        fourth_ingredients_list = []
        not_empty_string_3 = file.readline()
        fourth_key = file.readline().strip()
        count_fajitos = int(file.readline())
        for el in range(0, count_fajitos):
            prod3 = file.readline().strip().split('|')
            ingredients_for_fajitos = {'ingredient_name': prod3[0], 'quantity': prod3[1], 'measure': prod3[2]}
            res4 = ingredients_for_fajitos
            fourth_ingredients_list.append(ingredients_for_fajitos)
        # print(fourth_ingredients_list)

    cook_book = {key: ingredients_list, second_key: second_ingredients_list, third_key: third_ingredients_list,
                 fourth_key: fourth_ingredients_list}
    dish_dict = {}
    for dish in dishes:
        for cook_book_dish in cook_book[dish]:
            dish_dict_local = {}
            quantity_for_all = int(cook_book_dish['quantity']) * int(person_count)
            dish_dict_local['measure'] = cook_book_dish['measure']
            dish_dict_local['quantity'] = quantity_for_all
            # print(dish_dict_local)
            # print(quantity_for_all)
            if cook_book_dish['ingredient_name'] in dish_dict:
                dish_dict[cook_book_dish['ingredient_name']]['quantity'] += dish_dict_local['quantity']
            else:
                dish_dict[cook_book_dish['ingredient_name']] = dish_dict_local
    print(dish_dict)


get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 3)
