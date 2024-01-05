#      number1
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def __eq__(self, other):
#         return self.radius == other.radius
#     def __gt__(self, other):
#         return self.radius > other.radius
#     def __lt__(self, other):
#         return self.radius < other.radius
#     def __ge__(self, other):
#         return self.radius >= other.radius
#     def __le__(self, other):
#         return self.radius <= other.radius
#     def __add__(self, value):
#         return Circle(self.radius + value)
#     def __sub__(self, value):
#         return Circle(self.radius - value)
#     def __iadd__(self, value):
#         self.radius += value
#         return self
#     def __isub__(self, value):
#         self.radius -= value
#         return self
#
# c1 = Circle(8)
# c2 = Circle(4)
#
# print(c1 == c2)
# print(c1 < c2)
# print(c1 > c2)
#
# c1 -= 3
# c2 += 2
# print(c1.radius)
# print(c2.radius)

#  number2
# class Complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
#     def __add__(self, other):
#         return Complex(self.real + other.real, self.imag + other.imag)
#     def __sub__(self, other):
#         return Complex(self.real - other.real, self.imag - other.imag)
#     def __mul__(self, other):
#         real = self.real * other.real - self.imag * other.imag
#         imag = self.real * other.real + self.imag * other.imag
#         return Complex(real, imag)
#     def __truediv__(self, other):
#         a = other.real ** 2 + other.imag ** 2
#         real = (self.real * other.real - self.imag * other.imag) / a
#         imag = (self.real * other.real + self.imag * other.imag) / a
#         return Complex(real, imag)
#
# b = Complex(5, 8)
# c = Complex(2, 6)
#
# add = b + c
# sub = b - c
# mul = b * c
# div = b / c
# print(add.real + add.imag)
# print(sub.real + sub.imag)
# print(mul.real + mul.imag)
# print(div.real + div.imag)

#  number3
# class Airplane:
#     def __init__(self, model, max_pass, cur_pass):
#         self.model = model
#         self.max = max_pass
#         self.cur = cur_pass
#     def __eq__(self, other):
#         return self.model == other.model
#     def __add__(self, value):
#         self.cur += value
#         return self
#     def __sub__(self, value):
#         self.cur -= value
#         return self
#     def __iadd__(self, value):
#         self.cur += value
#         return self
#     def __isub__(self, value):
#         self.cur -= value
#         return self
#     def __gt__(self, other):
#         return self.max > other.max
#     def __lt__(self, other):
#         return self.max < other.max
#     def __ge__(self, other):
#         return self.max >= other.max
#     def __le__(self, other):
#         return self.max <= other.max
#
# a = Airplane('boeing 747', 450, 245)
# b = Airplane('airbus', 550, 383)
# print(a == b)
# print(a > b)
#
# a += 80
# b -= 40
# print(a.cur)
# print(b.cur)

#     number4
# class Flat:
#     def __init__(self, area, price):
#         self.area = area
#         self.price = price
#     def __eq__(self, other):
#         return self.area == other.area
#     def __ne__(self, other):
#         return self.area != other.area
#     def __gt__(self, other):
#         return self.price > other.price
#     def __lt__(self, other):
#         return self.price < other.price
#     def __ge__(self, other):
#         return self.price >= other.price
#     def __le__(self, other):
#         return self.price <= other.price
#
# a = Flat(130, 50000000)
# b = Flat(90, 30000000)
# print(a == b)
# print(a != b)
# print(a > b)