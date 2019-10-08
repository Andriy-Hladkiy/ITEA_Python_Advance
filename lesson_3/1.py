
class Example:
    def __init__(self, x):
        self._x = x

    def get_x(self):
        return self._x

    def __add__(self, other):
        return Example(
            self.get_x() + other.get_x()
        )

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __sub__(self, other):
        pass


a = Example(1)
b = Example(2)

c = a + b

print(c.get_x())
