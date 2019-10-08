class Example:
    def __init__(self, x):
        self._x = x

    def get_x(self):
        return self._x

    def __mul__(self, other):
        return Example(
            self.get_x() * other.get_x()
        )


x_one = Example(int(input('Enter x1')))
y_one = Example(int(input('Enter y1')))
z_one = Example(int(input('Enter z1')))
x_two = Example(int(input('Enter x2')))
y_two = Example(int(input('Enter y2')))
z_two = Example(int(input('Enter z3')))

x_result = x_one * x_two
y_result = y_one * y_two
z_result = z_one * z_two

print(x_result.get_x(), y_result.get_x(), z_result.get_x())
