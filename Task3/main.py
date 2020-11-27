import os

file_path_1 = os.path.join(os.getcwd(), '1.txt')
file_path_2 = os.path.join(os.getcwd(), '2.txt')
file_path_3 = os.path.join(os.getcwd(), '3.txt')
file_path_all_files = os.path.join(os.getcwd(), 'all_files.txt')

list_of_files = [file_path_1, file_path_2, file_path_3]

strings_in_1_file = 0
strings_in_2_file = 0
strings_in_3_file = 0
for one_file in list_of_files:
    with open(one_file) as f:
        lines = f.read().splitlines()
        if one_file == file_path_1:
            strings_in_1_file = len(lines)
            lines_1 = lines
        elif one_file == file_path_2:
            strings_in_2_file = len(lines)
            lines_2 = lines
        elif one_file == file_path_3:
            strings_in_3_file = len(lines)
            lines_3 = lines

page_list_of_files = [strings_in_1_file, strings_in_2_file, strings_in_3_file]
dict_pages_and_lines = {strings_in_1_file: lines_1, strings_in_2_file: lines_2, strings_in_3_file: lines_3}
dict_pages_and_names = {strings_in_1_file: file_path_1, strings_in_2_file: file_path_2, strings_in_3_file: file_path_3}
page_list_of_files = sorted(page_list_of_files)

with open(file_path_all_files, 'w') as general_file:
    for numb_of_pages in page_list_of_files:
        for line_numb, line_content in dict_pages_and_lines.items():
            if numb_of_pages == line_numb:
                for line_count, text_path in dict_pages_and_names.items():
                    if line_count == numb_of_pages:
                        file_name = os.path.basename(text_path)
                        general_file.write(file_name)
                        general_file.write('\n')
                general_file.write(str(line_numb))
                general_file.write('\n')
                for every_line in line_content:
                    general_file.write(every_line)
                    general_file.write('\n')


