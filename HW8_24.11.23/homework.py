#    number1
# def InsertionSort(A):
#     for i in range(1, len(A)):
#         list.sort(reverse = False)
#
# list = [3, 2, 5, 1, 8]
# InsertionSort(list)
# print(*list)

#      number2
# def SelectionSort(A):
#     for i in range(len(A)):
#         max = i
#         for j in range(i + 1, len(A)):
#             if A[j] > A[max]:
#                 max = j
#         A[i], A[max] = A[max], A[i]
#
# list = [1, 4, 2, 3, 4]
#
# SelectionSort(list)
# print(*list)

#        number3
# def min_amount(N, costs):
#     costs.sort(reverse=True)
#     total = sum(costs)
#     if N > 2:
#         total -= min(costs[:2])
#     return total
#
# N = 6
# costs = [1, 5, 4, 3, 5, 7]
#
# print(min_amount(N, costs))

#        number4
# def closest_numbers(list):
#     list.sort()
#
#     min_diff = float('inf')
#     closest = []
#
#     for i in range(len(list) - 1):
#         diff = list[i+1] - list[i]
#
#         if diff < min_diff:
#             min_diff = diff
#             closest = [list[i], list[i+1]]
#         elif diff == min_diff:
#             closest.extend([list[i], list[i+1]])
#
#     return closest
#
# numbers = [9, 4, 1, 6]
# print(*closest_numbers(numbers))