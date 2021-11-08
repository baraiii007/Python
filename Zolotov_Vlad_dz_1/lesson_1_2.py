
s = []

for i in range(1, 1000):
    if (i % 2 != 0):
        s.append(i)

print('List A:', s)

s3 = []
for x in s:
    x = x * x * x
    s3.append(x)

print(f'List B:', s3)

test = 0
for Chislo in s3:
    test = 0

    for simbol in str(Chislo):
        test += int(simbol)

    if (test % 7 == 0):
        print(Chislo)

for i in range(len(s3)):
    s3[i] = s3[i] + 17
print(s3)  # [5, 10, 15, 20, 25, 30]

test = 0
for Chislo in s3:
    test = 0

    for simbol in str(Chislo):
        test += int(simbol)

    if (test % 7 == 0):
        print(Chislo)