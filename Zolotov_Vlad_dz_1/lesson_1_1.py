a = input('Введите значение: ', )

sec = int(a) % 60
min = int(a) // 60
hour = int()
day = int()

while min // 60:
    if min >= 60:
        hour = hour + min // 60
        min = min % 60
    elif min < 60:
        min = min % 60

while hour // 24:
    if hour >= 24:
        day = day + hour // 24
        hour = hour % 24
    elif hour < 24:
        hour = hour % 24

print(a, ' это', day, 'дней', hour, 'час', min, 'мин', sec, 'сек')
