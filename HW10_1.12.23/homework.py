#   number1
#            из [1,2,3,4,5,6,7] получить {1: 1, 3: 27, 5: 125, 7: 343}
# list = [1,2,3,4,5,6,7]
# result = {x: x ** 3 for x in list if x % 2 != 0}
# print(result)

#            из [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7] получить {2, 4, 6}
# list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
# result = {x for x in list if x % 2 == 0}
# print(result)

#            получить список [0, 10, 20, 30, 40, 50, 60, 70, 80, 90] без исходного
# x = 10
# result = {i * 10 for i in range(x+1)}
# print(result)

#            написать функцию-генератор с yield, которая может перебирать числа, делящиеся на 7,
# в диапазоне от 0 до n.
# def fgenerator(n):
#     for i in range(n+1):
#         if i % 7 == 0:
#             yield i
#
# n = 80
# for x in fgenerator(n):
#     print(x)


#   number2
# from itertools import permutations
#
# input = "k98.ok"
# letters = [a for a in input if a.isalpha()]
#
# words = set()
# for i in range(1, len(letters) + 1):
#     for x in permutations(letters, i):
#         word = ''.join(x)
#         if word.isalpha() and word not in words:
#             words.add(word)
#
# words = sorted(words, key=lambda x: (len(x), x))
# print(len(words))
# for word in words:
#     print(word)