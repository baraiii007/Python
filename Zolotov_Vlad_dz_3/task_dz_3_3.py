def thesaurus(*args):
	count = 0

	for name in args:
		print(f'Получаем значение  = {name} из args \n')
		temp_list = name.split(' ')
		key_dict = temp_list[0][0]
		print(f'{key_dict} =  новый ключ')
		list_values = ''
		for item in args:
			_i = item.split(' ')
			# print(_i)
			if _i[0].startswith(key_dict):
				list_values += f'{item}, '
				print(f'получаем значения равные префику {key_dict} =  {list_values} \n')
			count += 1




thesaurus("Иван", "Мария", "Петр", "Илья")