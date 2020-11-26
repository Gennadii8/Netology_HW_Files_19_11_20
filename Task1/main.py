import os
file_path = os.path.join(os.getcwd(), 'recipes.txt')

with open(file_path) as f:
    lines = f.read().splitlines()
    dish_dictionary = {}
    dish_count = 1
    for one_line in lines:
        if one_line == '':
            dish_count += 1

    line_number = 0
    for i in range(dish_count):
        cook_book = []
        if lines[line_number] != '':
            dish_dictionary[lines[line_number]] = cook_book
            line_number += 1
            ingredient_count = int(lines[line_number])
            line_number += 1
            for element in range(ingredient_count):
                splitted_line = lines[line_number].split('|')
                one_ingredient_dict = {'ingredient_name': splitted_line[0], 'quantity': int(splitted_line[1]), \
                                       'measure': splitted_line[2]}
                cook_book.append(one_ingredient_dict)
                line_number += 1

        elif lines[line_number] == '':
            line_number += 1
            dish_dictionary[lines[line_number]] = cook_book
            line_number += 1
            ingredient_count = int(lines[line_number])
            line_number += 1
            for element in range(ingredient_count):
                splitted_line = lines[line_number].split('|')
                one_ingredient_dict = {'ingredient_name': splitted_line[0], 'quantity': int(splitted_line[1]), \
                                       'measure': splitted_line[2]}
                cook_book.append(one_ingredient_dict)
                line_number += 1
    print(dish_dictionary)

    def get_shop_list_by_dishes(dishes, person_count):
        order_dish_dictionary = {}
        for dish in dishes:
            for dish_name in dish_dictionary.keys():
                if dish_name == dish:
                    ingredients_of_dish = dish_dictionary.get(dish_name)
                    for one_ing in ingredients_of_dish:
                        order_param_of_ing = {}
                        if one_ing['ingredient_name'] in order_dish_dictionary:
                            for name, ing in order_dish_dictionary.items():
                                if one_ing['ingredient_name'] == name:
                                    copy_one_ing = one_ing['quantity'] * person_count
                                    order_param_of_ing['measure'] = one_ing['measure']
                                    order_param_of_ing['quantity'] = ing['quantity'] + copy_one_ing
                                    order_dish_dictionary.update({one_ing['ingredient_name']: order_param_of_ing})
                        else:
                            one_ing['quantity'] *= person_count
                            order_param_of_ing['measure'] = one_ing['measure']
                            order_param_of_ing['quantity'] = one_ing['quantity']
                            order_dish_dictionary.setdefault(one_ing['ingredient_name'], order_param_of_ing)
                            # order_dish_dictionary[one_ing['ingredient_name']] = order_param_of_ing

        print(order_dish_dictionary)


    order_dishes = ['Фахитос', 'Омлет']
    order_persons = 3

    get_shop_list_by_dishes(order_dishes, order_persons)


