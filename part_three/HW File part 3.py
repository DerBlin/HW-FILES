character_file = []
with open('1.txt', encoding='utf-8') as file:
    character_file_1 = []
    lines1 = file.readlines()
    character_file_1.append(len(lines1))
    character_file_1.append(lines1)
    character_file_1.append('1.txt')
    character_file.append(character_file_1)
with open('2.txt', encoding='utf-8') as file:
    character_file_2 = []
    lines2 = file.readlines()
    character_file_2.append(len(lines2))
    character_file_2.append(lines2)
    character_file_2.append('2.txt')
    character_file.append(character_file_2)
    # print(len(lines2))
with open('3.txt', encoding='utf-8') as file:
    character_file_3 = []
    lines3 = file.readlines()
    character_file_3.append(len(lines3))
    character_file_3.append(lines3)
    character_file_3.append('3.txt')
    character_file.append(character_file_3)
count_str_list = []
for character in character_file:
    count_str_list.append(character[0])
count_str_list.sort()
# print(count_str_list)
with open('result.txt', 'w', encoding='utf-8') as f:
    for count in count_str_list:
        for character in character_file:
            if count == character[0]:
                f.write(f'{str(character[2])}\n')
                f.write(f'{str(character[0])}\n')
                for string in character[1]:
                    f.write(f'{str(string).strip()}\n')

