import math

length = float(input('Сторона квадрата: '))
p = length * 4
s = length ** 2
d = length * math.sqrt(2)

p = round(p, 2)
s = round(s, 2)
d = round(d, 2)

print(str(p) + ",", str(s) + ",", str(d))