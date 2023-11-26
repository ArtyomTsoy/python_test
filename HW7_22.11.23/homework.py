# #   number1
# import math
#
#
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# def fibonacci(n):
#     if n <= 0:
#         return "Введите число больше 0"
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# operations = {
#     '+': lambda x, y: x + y,
#     '-': lambda x, y: x - y,
#     '*': lambda x, y: x * y,
#     '/': lambda x, y: x / y,
#     '^': lambda x, y: x ** y,
#     'sin': lambda x: math.sin(x),
#     'cos': lambda x: math.cos(x),
#     'tan': lambda x: math.tan(x),
#     'factorial': factorial,
#     'fibonacci': fibonacci
# }
#
# print("Доступные операции:")
# print("+, -, *, /, ^, sin, cos, tan, factorial, fibonacci")
#
# while True:
#     operation = input("Выберите операцию (или 'exit' для выхода): ").lower()
#     if operation == 'exit':
#         break
#
#     if operation in operations:
#         if operation in ['sin', 'cos', 'tan']:
#             num = float(input("Введите число: "))
#             result = operations[operation](num)
#         elif operation in ['factorial', 'fibonacci']:
#             num = int(input("Введите число: "))
#             result = operations[operation](num)
#         else:
#             num1 = float(input("Введите первое число: "))
#             num2 = float(input("Введите второе число: "))
#             result = operations[operation](num1, num2)
#
#         print(f"Результат операции {operation}: {result}")
#     else:
#         print("Некорректная операция. Пожалуйста, выберите из доступных операций.")

#         number2
# def print_board(board):
#     for row in board:
#         print("|".join(row))
#     print("-------------")
#
# def check_winner(board, player):
#     for row in board + [list(row) for row in zip(*board)] + [[board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]]:
#         if all(cell == player for cell in row):
#             return True
#     return False
#
# def play_game():
#     print("********** Игра Крестики-нолики для двух игроков **********")
#     board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
#     player = "X"
#
#     while True:
#         print_board(board)
#         move = input(f"Куда поставим {player}? ")
#
#         for i, row in enumerate(board):
#             if move in row:
#                 board[i][row.index(move)] = player
#
#         if check_winner(board, player):
#             print_board(board)
#             print(f"{player} выиграл!")
#             break
#
#         player = "O" if player == "X" else "X"
#
# if __name__ == "__main__":
#     play_game()

#       number3
# from collections import Counter
#
# candidates = ["Аскаров", "Бекмуханов", "Ернур", "Пешая", "Карим", "Шаримазданов"]  # ваш список кандидатов
# votes = []
#
# while True:
#     vote = input("Вы отдаете голос за (или 'exit' для завершения голосования): ")
#     if vote.lower() == 'exit':
#         break
#     if vote in candidates:
#         votes.append(vote)
#     else:
#         print("Неверный кандидат. Пожалуйста, выберите из списка кандидатов.")
#
# vote_counts = Counter(votes)
# max_votes = max(vote_counts.values())
# winners = [candidate for candidate, count in vote_counts.items() if count == max_votes]
#
# if len(winners) > 1:
#     winners.sort(key=lambda x: (len(x), x))
#     winner = winners[0]
# else:
#     winner = winners[0]
#
# print(f"Победитель выборов: {winner}. Количество голосов: {max_votes}.")
