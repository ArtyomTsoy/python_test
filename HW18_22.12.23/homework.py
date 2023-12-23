class Main:
    def __init__(self, text):
        self._text = text
    def set_text(self, text=None):
        if text:
            self._text = text
        else:
            print('main text')
    def get_text(self):
        return self._text

class Child(Main):
    def __init__(self, text, number):
        super().__init__(text)
        self._number = number
    def set_number(self, number):
        self._number = number
    def get_number(self):
        return self._number

a = Main('text')
print(a.get_text())

a.set_text('new text')
print(a.get_text())

b = Child('child', 8)
print(b.get_text())
print(b.get_number())

b.set_number(20)
print(b.get_number())
