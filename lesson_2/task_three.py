class Example:
    def __init__(self, value):
        self._x = value
        self._y = value
        self._z = value

    def set_x(self, value):
        self._x = value

    def get_x(self):
        return self._x

    def set_y(self, value):
        self._y = value

    def get_y(self):
        return self._y

    def set_z(self, value):
        self._z = value

    def get_z(self):
        return self._z

    def __mul__(self, other):
        return Example(
            self.get_x() * other.get_x()
        )


x_one = Example(int(input('Enter x1:\n')))
y_one = Example(int(input('Enter y1:\n')))
z_one = Example(int(input('Enter z1:\n')))
x_two = Example(int(input('Enter x2:\n')))
y_two = Example(int(input('Enter y2:\n')))
z_two = Example(int(input('Enter z2:\n')))

x_result = x_one * x_two
y_result = y_one * y_two
z_result = z_one * z_two

print(x_result.get_x(), y_result.get_y(), z_result.get_z())
