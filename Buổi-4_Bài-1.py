import random

greeting = ['Hello', 'Hi', 'Chào', 'Xin chào']
name = input('Nhập tên của bạn: ')
gender = input('Nhập cách xưng hô của bạn: ')
birth_year = int(input('Nhập năm sinh của bạn: '))
current_year = 2022

def calculator_zodiac(year):
    zodiac = ['Chuột', 'Trâu', 'Hổ', 'Mèo', 'Rồng', 'Rắn', 'Ngựa', 'Dê', 'Khỉ', 'Gà', 'Chó', 'Lợn']
    position = 4
    return zodiac[(year - position) % 12]

zodiac = calculator_zodiac(birth_year)
age = current_year - birth_year
random_greeting = random.choice(greeting)
message = [f'{random_greeting} {gender} {name}, {gender} {age} tuổi à.', f'{random_greeting} {gender} {name}, {gender} tuổi con {zodiac} à.']

print(random.choice(message))
