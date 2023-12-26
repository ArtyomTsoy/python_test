#    number1
# class Device:
#     def __init__(self, info):
#         self.info = info
#     def device(self, info):
#         return 'turn on'
#
# class CoffeeMachine(Device):
#     def __init__(self, info):
#         super().__init__(info)
#     def coffee(self):
#         return 'produce coffee'
#
# class Blender(Device):
#     def __int__(self, info):
#         super().__init__(info)
#     def blender(self):
#         return 'mix ingridients'
#     def cof(self):
#         if hasattr(self, 'coffee'): self.coffee()
#         else: print('blender cant produce coffee')
#
# class MeatGrinder(Device):
#     def __init__(self, info):
#         super().__init__(info)
#     def meatgrinder(self):
#         return 'cut a meat into tiny pieces'
#
# blender = Blender('mix fruits')
# print (blender.cof())

#       number2
# class Ship:
#     def __init__(self, info, is_fast, is_maneuverable):
#         self.info = info
#         self.speed = is_fast
#         self.maneuverability = is_maneuverable
#     def ship(self):
#         return 'can swim'
#
# class Frigate(Ship):
#     def __init__(self, info):
#         super().__init__(info, True, True)
#     def frigate(self):
#         return 'full-rigged ship built for speed and maneuverability'
#
# class Destroyer(Ship):
#     def __init__(self, info):
#         super().__init__(info, True, True)
#     def destroyer(self):
#         return 'fast, maneuverable, long-endurance warship'
#
# class Cruiser(Ship):
#     def __init__(self, info):
#         super().__init__(info, True, False)
#     def cruiser(self):
#         return 'large surface warship built for high speed'
#
#     def maneuverable(self):
#         if hasattr(self, 'is_maneuverable'): self.maneuverability
#         else: print('not maneuverable')
#
# new_ship = Cruiser('warship')
# new_ship.maneuverable()

#          number3
# class Square:
#     def __init__(self, length):
#         self.length = length
#     def areaS(self):
#         return self.length * 2
#
# class Circle:
#     def __init__(self, length):
#         self.radius = length / 2
#     def areaC(self):
#         return 3.14 * self.radius ** 2
#
# class InscribedCircle(Square, Circle):
#     def __init__(self, length):
#         Square.__init__(self, length)
#         Circle.__init__(self, length)
#
# inscribed = InscribedCircle(3)
# print('square:', inscribed.areaS())
# print('circle square:', inscribed.areaC())

#      number4
# class Wheels:
#     def __init__(self, number_wheels):
#         self.wheels = number_wheels
#     def rotate(self):
#         return 'wheels rotating'
#
# class Engine:
#     def __init__(self, fuel_type):
#         self.fuel = fuel_type
#     def start(self):
#         return 'engine started'
#
# class Doors:
#     def __init__(self, number_doors):
#         self.doors = number_doors
#     def open(self):
#         return 'doors opened'
#
# class Car(Wheels, Engine, Doors):
#     def __init__(self, wheels, fuel, doors):
#         Wheels.__init__(self, wheels)
#         Engine.__init__(self, fuel)
#         Doors.__init__(self, doors)
#
# car = Car(4, 'gasoline', 4)
# print(car.rotate())
# print(car.start())
# print(car.open())

#      number5
import pickle

class Shape:
    def __init__(self):
        pass
    def show(self):
        pass
    def save(self, workplace):
        with open(workplace, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load(workplace):
        with open(workplace, 'rb') as file:
            return pickle.load(file)

class Square(Shape):
    def __init__(self, x, y, length):
        super().__init__()
        self.x = x
        self.y = y
        self.length = length
    def show(self):
        return 'squares x={self.x}, y={self.y}, length={self.length}'

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def show(self):
        return 'rectangles x={self.x}, y={self.y}, width={self.width}, height={self.height}'

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
    def show(self):
        return 'circles x={self.x}, y={self.y}, radius={self.radius}'

class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def show(self):
        return 'rectangles x={self.x}, y={self.y}, width={self.width}, height={self.height}'

shapes = [
    Square(3,4,6),
    Rectangle(4,6,7,9),
    Circle(1,1,4),
    Ellipse(2,3,7,5)
]

with open('shapes.pickle', 'wb') as file:
    pickle.dump(shapes, file)
with open('shapes.pickle', 'rb') as file:
    loaded = pickle.load(file)
for shape in loaded:
    shape.show()
