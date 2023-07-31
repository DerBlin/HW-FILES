
flag = 0
key = None
count_dish = 0
inner_dict = {}
row_counter = 0
ingredients = {}
cook_book = {}
with open('recipes.txt', encoding='utf-8') as file:
    for el in file.readlines():
        if flag == 0:
            key = el
            flag = 1
            # print(flag)
            # print(el)
            continue
        if flag == 1:
            ingredients_list = []
            count_dish = int(el)
            flag = 2
            # print(flag)
            # print(el)
            continue
        if flag == 2 and count_dish > row_counter:
            # print(el)
            prod = el.strip().split('|')
            ingredients_list.append({'ingredient_name': prod[0], 'quantity': prod[1], 'measure': prod[2]})
            row_counter += 1
            continue
        if flag == 2 and count_dish == row_counter:
            cook_book = {key.strip(): ingredients_list}
            print(cook_book)
            flag = 0
            key = None
            count_dish = 0
            inner_dict = {}
            row_counter = 0
            ingredients.clear()
            ingredients_list.clear()
            continue
cook_book = {key.strip(): ingredients_list}
print(cook_book)



