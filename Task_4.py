# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

S = int(input('Сколько всего журавливок было сделано: '))
print('Петя и Серёжа сделали по', int(S/6), 'журавликов. А Катя -', int(S*4/6))
