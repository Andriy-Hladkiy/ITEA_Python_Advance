class Vehicle:
    FUEL_TYPE = 'Diesel'

    def set_fuel(self, value):
        self._fuel += value

    def get_fuel(self):
        return self._fuel

    def set_brand(self, value):
        self._brand = value

    def get_brand(self):
        return self._brand

    def set_size_of_wheels(self, value):
        self._size_of_wheels = value

    def get_size_of_wheel(self):
        return self._size_of_wheels


class Truck:
    FUEL_TYPE = 'Diesel'
    NUM_OF_DOORS = 2

    def set_weight_of_cargo(self, value):
        self._weight_of_cargo += value

    def get_weight_of_cargo(self):
        return self._weight_of_cargo

    def set_destination(self, value):
        self._destination = value

    def get_destination(self):
        return self._destination


class Car(Vehicle, Truck):

    def __init__(self, fuel, brand, size_of_wheels, weight_of_cargo, destination):
        self._fuel = fuel
        self._brand = brand
        self._size_of_wheels = size_of_wheels
        self._weight_of_cargo = weight_of_cargo
        self._destination = destination


car = Car(10, 'Lada', 13, 3000, 'Kiev')
print(car.get_fuel())
print(car.get_brand())
print(car.get_size_of_wheel())
print(car.get_weight_of_cargo())
print(car.get_destination())
