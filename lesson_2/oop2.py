# Наследование
class Vehicle:
    NUM_OF_DOORS = 4
    FUEL_TYPE = 'GAS'

    def move(self):
        print('Car drives')

    def set_fuel(self, value):
        self._fuel += value

    def get_fuel(self):
        return self._fuel

    def get_brand(self):
        return self._brand

    def set_brand(self, value):
        self._brand = value

    def get_engine(self):
        return self._engine

    def set_engine(self, value):
        self._brand = value

    def __str__(self):
        return f'Brand is {self._brand} and engine is {self._engine}'


class Car(Vehicle):

    def __init__(self, brand, engine):
        self._brand = brand
        self._engine = engine
        self._fuel = 0

    def move(self):  # Полиморфизм
        print('Move about 100km per hour')


car = Car('bmw', 'v8')
print(car.get_brand())
car.move()

print(car)


class Example:
    __slots__ = ('_name')

    def __init__(self, name):
        self._name = name


obj = Example('example objects')

obj._name = 'new_name'
#bj._my_cool_var = 11  # добавляти перемені не можна через __slots__ буде ошибка
