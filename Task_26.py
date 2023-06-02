# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def deg(a, b):
    if b == 0:
        return 1
    if b > 0:
        return a*deg(a, b-1)
    else:
        return 1/a*deg(a, b+1)


A = int(input('Введите число: '))
B = int(input('Введите cтепень числа: '))
print(f'{A}^{B}={deg(A,B)}')
