x = int(input())
y = int(input())
z = int(input())
s = 0
x1 = str(x)
x1 = x1[::-1]

if y == 10:
    s = ''
    while x != 0:
        s = str(x % z) + str(s)
        x //= z

if y != 10:
    s = 0
    for i in range(0, len(x1)):
        s += int(x1[i]) * (y ** i)

if y != 10 and z != 10:
    s1 = ''
    while s != 0:
        s1 = str(s % z) + str(s1)
        s //= z
    s = s1

if y == z:
    s = ('Вы ввели одинаковые системы счисления')
if y == 0 or z == 0:
    s = ('Некорректные данные')
x1 = str(x)
for i in range(1, len(x1) + 1):
    if int(x1[i - 1]) >= y:
        s = ('Некорректные данные')
        break
    elif i == int(len(x1)):
        s = s
print(s)
