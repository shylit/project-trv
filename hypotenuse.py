import math

a = float(input("Введите длину первого катета: "))
b = float(input("Введите длину второго катета: "))

c = math.sqrt(a ** 2 + b ** 2)

print("Длина гипотенузы:", c)
