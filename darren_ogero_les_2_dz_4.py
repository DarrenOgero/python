name_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']

name_str_one = name_list[0]
str_one_parts = name_str_one.split(' ')

name_str_two = name_list[1]
str_two_parts = name_str_two.split(' ')

name_str_three = name_list[2]
str_three_parts = name_str_three.split(' ')

name_str_four = name_list[3]
str_four_parts = name_str_four.split(' ')

print('Привет,', str_one_parts[1].title())

print('Привет,', str_two_parts[2].title())

print('Привет,', str_three_parts[3].title())

print('Привет,', str_four_parts[1].title())


