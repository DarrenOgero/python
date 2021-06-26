temp_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

temp_list.insert(2, '05')
temp_list.pop(1)

temp_list.pop(8)
temp_list.insert(8, '+05')

temp_list.insert(2, '"')
temp_list.insert(1, '"')
temp_list.insert(5, '"')
temp_list.insert(7, '"')
temp_list.insert(12, '"')
temp_list.insert(14, '"')

print(temp_list[0], temp_list[1]+temp_list[2]+temp_list[3], temp_list[4],
      temp_list[5]+temp_list[6]+temp_list[7], temp_list[8], temp_list[9],
      temp_list[10], temp_list[11], temp_list[12]+temp_list[13]+temp_list[14],
      temp_list[15])