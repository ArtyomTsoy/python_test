#       number1
# a = int(input("Введите количество биологов: "))
# b = int(input("Введите количество информатиков: "))
#
# d = 1
# while True:
#     if d % a == 0 and d % b:
#         break
#     d += 1
#
# print("Наименьшее число кусочков: ", d)

#          number2
# n = int(input("Введите число: "))
# factorial = 1
# sum_factorial = 0
#
# for i in range(1, n + 1):
#     factorial *= i
#     sum_factorial += factorial
#
# print("Сумма факториалов от 1 до", n, ":", sum_factorial)

#          number3
# n = int(input("Введите цифру: "))
#
# if n <= 9:
#     for i in range(1, n + 1):
#         for j in range(1, i + 1):
#             print(j, end="")
#         print()
# else:
#     print("Это число больше 9")

#       number4
# n = int(input("Введите общее число карточек: "))
# remaining = list(map(int, input("Введите номера оставшихся карточек через пробел: ").split()))
#
# missing = 0
# for i in range(1, n + 1):
#     if i not in remaining:
#         missing = i
#         break
#
# print("Потерянная карточка: ", missing)

#       number5
# n = int(input("Введите число: "))
# i = 1
#
# while i ** 2 <= n:
#     print(i ** 2)
#     i += 1