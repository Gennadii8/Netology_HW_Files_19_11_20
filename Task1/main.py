import os
# print(os.getcwd())
file_path = os.path.join(os.getcwd(), 'recipes.txt')
# print(file_path)

with open(file_path) as f:
    lines = f.read().splitlines()
    dish_dictionary = {}
    # print(type(lines))
    # print(len(lines))
    # print(lines[1])
    # print(lines)
    # dish_dictionary = {lines[0]: cook_book}
    # ingredient_count = int(lines[1])
    # print(ingredient_count)
    # print(type(ingredient_count))
    dish_count = 1
    for one_line in lines:
        if one_line == '':
            dish_count += 1
    # print(dish_count)

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
                # print(splitted_line)
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
                # print(splitted_line)
                one_ingredient_dict = {'ingredient_name': splitted_line[0], 'quantity': int(splitted_line[1]), \
                                       'measure': splitted_line[2]}
                cook_book.append(one_ingredient_dict)
                line_number += 1
    print(dish_dictionary)

