# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

n = int(input('Введите количество элементов первого множества: '))
first_set = []
for i in range(n):
    first_set.append(int(input(f'Введите {i+1} элемент множества: ')))
m = int(input('Введите количество элементов второго множества: '))
second_set = []
for i in range(m):
    second_set.append(int(input(f'Введите {i+1} элемент множества: ')))
print(sorted(set(first_set) & set(second_set)))
