# Хоть работа и выполнена через chatgpt я в подробностях рассмотрел каждую частичку кода и что не понимал спрашивал у того же самого
# чата gtp. Все непонятные мне части я подробно разбирал дабы не потерять суть и смысл самого кода.

#    number1
# def count_odd_even(lst):
#     odd_numbers = [num for num in lst if num % 2 != 0]
#     even_numbers = [num for num in lst if num % 2 == 0]
#
#     if len(odd_numbers) > len(even_numbers):
#         return odd_numbers, even_numbers, "NO"
#     else:
#         return odd_numbers, even_numbers, "YES"
#
# def main():
#     N = int(input("Введите длину списка: "))
#     user_list = list(map(int, input("Введите числа через пробел: ").split()))
#
#     odd, even, result = count_odd_even(user_list)
#     print(" ".join(map(str, odd)))
#     print(" ".join(map(str, even)))
#     print(result)
#
#
# if __name__ == "__main__":
#     main()

#    number2
# def create_3x3_matrix():
#     matrix = []
#     print("Введите элементы матрицы 3x3:")
#     for i in range(3):
#         row = list(map(int, input().split()))
#         matrix.append(row)
#     return matrix
#
# def sum_main_diagonal(matrix):
#     diagonal_sum = 0
#     for i in range(len(matrix)):
#         diagonal_sum += matrix[i][i]
#     return diagonal_sum
#
# def main():
#     matrix = create_3x3_matrix()
#     diagonal_sum = sum_main_diagonal(matrix)
#     print(f"Сумма элементов главной диагонали: {diagonal_sum}")
#
# if __name__ == "__main__":
#     main()

#       number3
# def get_user_data():
#     name = input("Введите ваше имя: ")
#     age = input("Введите ваш возраст: ")
#     email = input("Введите ваш email: ")
#     phone = input("Введите ваш номер телефона: ")
#     experience = input("Введите ваш опыт работы: ")
#     education = input("Введите ваше образование: ")
#
#     user_data = {
#         "Имя": name,
#         "Возраст": age,
#         "Email": email,
#         "Телефон": phone,
#         "Опыт работы": experience,
#         "Образование": education
#     }
#     return user_data
#
# def display_cv(data):
#     print("\n--- Ваше резюме ---")
#     for key, value in data.items():
#         print(f"{key}: {value}")
#
# def main():
#     user_info = get_user_data()
#     display_cv(user_info)
#
# if __name__ == "__main__":
#     main

#    number4
# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# def main():
#     number = int(input("Введите номер числа Фибоначчи: "))
#     for i in range(1, number + 1):
#         print(f"fibonacci number {i} = {fibonacci(i)}")
#
# if __name__ == "__main__":
#     main()

#      number5
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

number = int(input("Введите число: "))
result = is_power_of_two(number)
print(f"Является ли число степенью двойки: {result}")