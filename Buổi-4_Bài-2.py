list = '[12, 25, 38, 18, 16]'
clear_list = list.replace(',', '').replace('[', '').replace(']', '')
list_number = clear_list.split()

for number in list_number:
    print(number)
