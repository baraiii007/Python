a = input('Введите значение:', )

sec = float(a) % 60
min = float(a) // 60
print(a, ' это', min, 'мин', sec, 'сек')
