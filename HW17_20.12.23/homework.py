#      number1
# class Car:
#     def __init__(self, a_model, a_year, a_manufacturer, a_colour, a_capacity, a_price):
#         self.model = a_model
#         self.year = a_year
#         self.manuf = a_manufacturer
#         self.colour = a_colour
#         self.capacity = a_capacity
#         self.price = a_price
#
#     def setYear(self, a_year):
#         self.__year = a_year
#     def getYear(self):
#         return self.__year
#
# Mercedes = Car('cls 63 amg', 2017, 'Mercedes', 'black', 6.2, 108000) # in dollars
# print(Mercedes.model)

#     number2
# class Book:
#     def __init__(self, a_name, a_year, a_publisher, a_genre, a_author, a_price):
#         self.name = a_name
#         self.year = a_year
#         self.publisher = a_publisher
#         self.genre = a_genre
#         self.author = a_author
#         self.price = a_price
#     def setPrice(self, a_price):
#         self.__price = a_price
#     def getPrice(self):
#         return self.__price
#
# Kafka = Book('Kafka on the beach', 2002, 'Murakami mania', 'fantasy', 'Haruki Murakami', 2640)
# print(Kafka.publisher)

#     number3
# class Stadium:
#     def __init__(self, a_name, a_date, a_country, a_city, a_capacity):
#         self.name = a_name
#         self.date = a_date
#         self.country = a_country
#         self.city = a_city
#         self.capacity = a_capacity
#     def setDate(self, a_date):
#         self._date = a_date
#     def getDate(self):
#         return self._date
#
# football = Stadium('Barcelona', 1987, 'Catalonia', 'Barcelona', 900000)
# print(football.city)

#     number4
# class Main:
#     def __init__(self, argtext):
#         self.argtext = argtext
#     def set_argtext(self, new_text=None):
#         if new_text:
#             self.argtext = new_text
#         else:
#             self.argtext = 'text'
#
# class ChildClass(Main):
#     def __init__(self, argtext, argnumber):
#         super().__init__(argtext)
#         self.argnumber = argnumber
#
# a = Main('new text')
# print(a.argtext)
#
# a.set_argtext('another one')
# print(a.argtext)
#
# b = ChildClass('childclass text', 10)
# print(b.argtext)
# print(b.argnumber)

