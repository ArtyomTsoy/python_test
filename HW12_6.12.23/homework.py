#     number1
# def filter_text(input_file, bad_words_file, output_file):
#     with open(input_file, 'r') as file:
#         text = file.read()
#
#     with open(bad_words_file, 'r') as bad_file:
#         bad_words = bad_file.read().splitlines()
#
#     for word in bad_words:
#         text = text.replace(word, '')
#
#     with open(output_file, 'w') as new_file:
#         new_file.write(text)
#
# input_file_path = 'C:/github/ArtyomTsoy/HW12_6.12.23/text.txt'
# bad_words_file_path = 'C:/github/ArtyomTsoy/HW12_6.12.23/bad_words.txt'
# output_file_path = 'filtered.txt'
#
# filter_text(input_file_path, bad_words_file_path, output_file_path)

#       number2
# def transliterate(text, translit_dict):
#     return ''.join(translit_dict.get(char, char) for char in text)
#
#
# def load_translit_dict(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         return dict(line.strip().split(',') for line in file)
#
#
# def save_to_file(text, output_file):
#     with open(output_file, 'w', encoding='utf-8') as file:
#         file.write(text)
#
#
# def main():
#     direction = input("Выберите направление перевода (1 - русский -> английский, 2 - английский -> русский): ")
#
#     if direction == '1':
#         input_file = 'translit_ru_en.txt'
#         output_file = 'transliterated_en.txt'
#     elif direction == '2':
#         input_file = 'translit_en_ru.txt'
#         output_file = 'transliterated_ru.txt'
#     else:
#         print("Неверный выбор направления.")
#         return
#
#     translit_dict = load_translit_dict(input_file)
#
#     text = input("Введите текст для транслитерации: ")
#     transliterated_text = transliterate(text, translit_dict)
#     save_to_file(transliterated_text, output_file)
#
#
# if __name__ == "__main__":
#     main()

#       number3
# def connected_files(input_file, output_file):
#     with open(output_file, 'w') as output:
#         for file_name in input_file:
#             with open(file_name, 'r') as file:
#                 content = file.read()
#                 output.write(content)
#
# def main():
#     input_file = []
#     while True:
#         file_name = input("Введите название файла или 'quit' для завершения: ")
#         if file_name.lower() == 'quit':
#             break
#         input_file.append(file_name)
#
#     if len(input_file) == 0:
#         print("Не введено ни одного файла.")
#         return
#
#     output_file = 'merged_output.txt'
#     connected_files(input_file, output_file)
#
# if __name__ == "__main__":
#     main()

#        number4
# def get_common_characters(files):
#     common_characters = set()
#
#     # Читаем первый файл, чтобы получить начальный набор символов
#     with open(files[0], 'r', encoding='utf-8') as first_file:
#         common_characters = set(first_file.read())
#
#     # Перебираем остальные файлы и определяем общие символы
#     for file_name in files[1:]:
#         with open(file_name, 'r', encoding='utf-8') as file:
#             characters = set(file.read())
#             common_characters = common_characters.intersection(characters)
#
#     return common_characters
#
#
# def main():
#     file_names = []
#     while True:
#         file_name = input("Введите название файла или 'quit' для завершения: ")
#         if file_name.lower() == 'quit':
#             break
#         file_names.append(file_name)
#
#     if len(file_names) == 0:
#         print("Не введено ни одного файла.")
#         return
#
#     common_chars = get_common_characters(file_names)
#
#     if len(common_chars) == 0:
#         print("Нет общих символов во всех файлах.")
#         return
#
#     output_file = 'common_characters.txt'
#     with open(output_file, 'w', encoding='utf-8') as file:
#         file.write(''.join(common_chars))
#
#     print(f"Символы, которые есть во всех файлах, записаны в {output_file}")
#
#
# if __name__ == "__main__":
#     main()

#        number5
# import os
# import shutil
#
# current_directory = os.getcwd()
#
# video_directory = os.path.join(current_directory, 'video')
# sub_directory = os.path.join(current_directory, 'sub')
# watch_me_directory = os.path.join(current_directory, 'watch_me')
#
# if not os.path.exists(watch_me_directory):
#     os.mkdir(watch_me_directory)
#
# for folder in [video_directory, sub_directory]:
#     for file_name in os.listdir(folder):
#         file_path = os.path.join(folder, file_name)
#         if os.path.isfile(file_path):
#             shutil.move(file_path, watch_me_directory)
#
# print("Содержимое папок video и sub перемещено в папку watch_me.")

#        number6
# import os
#
# files = os.listdir()
#
# for file_name in files:
#     if file_name.endswith('.jpg'):
#         parts = file_name.split('_')
#         if len(parts) == 2:
#             new_name = f"{parts[1]}_{parts[0]}"
#             os.rename(file_name, new_name)
#             print(f"Файл {file_name} переименован в {new_name}")
#         else:
#             print(f"Файл {file_name} не изменен, так как не соответствует формату имени_фамилия.jpg")
#     else:
#         print(f"Файл {file_name} не является изображением в формате jpg и не изменен.")

#        number7
# import os
#
# current_directory = os.getcwd()
#
# list_file_path = os.path.join(current_directory, 'list.tsv')
#
# list_directory = os.path.join(current_directory, 'list')
# if not os.path.exists(list_directory):
#     os.mkdir(list_directory)
#
# with open(list_file_path, 'r', encoding='utf-8') as file:
#     file_names = file.read().splitlines()
#
# for file_name in file_names:
#     file_path = os.path.join(current_directory, file_name)
#     if os.path.exists(file_path):
#         target_path = os.path.join(list_directory, file_name)
#         os.rename(file_path, target_path)
#         print(f"Файл {file_name} перемещен в папку list")
#     else:
#         print(f"Файл {file_name} не найден в текущей директории и не перемещен")

#     number8
# def remove_last_line(input_file, output_file):
#     with open(input_file, 'r', encoding='utf-8') as file:
#         lines = file.readlines()
#
#     if len(lines) > 0:
#         lines = lines[:-1]
#
#         with open(output_file, 'w', encoding='utf-8') as new_file:
#             new_file.writelines(lines)
#             print(f"Последняя строка удалена. Результат сохранен в файле {output_file}")
#     else:
#         print("Файл пуст, невозможно удалить последнюю строку.")
#
#
# input_file_path = 'input.txt'
# output_file_path = 'output.txt'
#
# remove_last_line(input_file_path, output_file_path)