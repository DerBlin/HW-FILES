import os, fnmatch
directory = "C:\\Users\\ewbli\\OneDrive\\Рабочий стол\\HW Files\\DONE\\part_three\\text"
listOfFiles = os.listdir(directory)
pattern = "*.txt"
name_list = []
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        name_list.append(entry)
dictionary = {}
for name in name_list:
    with open(name, encoding='utf-8') as file:
        temp_list = []
        lines1 = file.readlines()
        temp_list.append(len(lines1))
        temp_list.append(lines1)
        temp_list.append(name)
        dictionary[name] = temp_list
with open('result.txt', 'w', encoding='utf-8') as f:
    for item in sorted(dictionary.values()):
        f.write(f'{str(item[2])}\n')
        f.write(f'{str(item[0])}\n')
        for string in item[1]:
            f.write(f'{str(string).strip()}\n')