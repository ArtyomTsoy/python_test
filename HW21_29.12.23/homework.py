class Roman:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return Roman(self.to_roman(self.to_int(self.value) + self.to_int(other.value)))
    def __sub__(self, other):
        return Roman(self.to_roman(self.to_int(self.value) - self.to_int(other.value)))
    def __mul__(self, other):
        return Roman(self.to_roman(self.to_int(self.value) * self.to_int(other.value)))
    def __truediv__(self, other):
        return Roman(self.to_roman(self.to_int(self.value) // self.to_int(other.value)))

    @staticmethod
    def to_int(roman):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0
        for numeral in roman[::-1]:
            value = roman_dict[numeral]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
        return result

    @staticmethod
    def to_roman(num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        while num > 0:
            for k in range(num // val[i]):
                roman_num += syms[i]
                num -= val[i]
            i += 1
        return roman_num

a = Roman('XII')
b = Roman('IV')

add = a + b
sub = a - b
mul = a * b
div = a / b

print(add.value)
print(sub.value)
print(mul.value)
print(div.value)