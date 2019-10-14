class Example:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

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
            self.get_x() * other.get_x(),
            self.get_y() * other.get_y(),
            self.get_z() * other.get_z()
        )


point1 = Example(1, 3, 5)
point2 = Example(5, 7, 3)

result_point = point1 * point2

print(result_point.get_x(), result_point.get_y(), result_point.get_z())
