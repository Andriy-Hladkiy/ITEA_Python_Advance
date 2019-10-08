# class Cat:
#     CATS_CREATED = 0
#
#
#     def __init__(self, color, name):
#         self._name = name
#         self._color = color
#         Cat.CATS_CREATED += 1
#
#     def say_meow(self):
#         print('MEOW!')
#
#     def walk_around(self):
#         print('The cat walks around')
#
#     def eat(self):
#         print('Cat eats')
#
#     # def what_is_the_self(self):
#     #     print(self)
#     #
#     # def test_self(self):
#     #     print('trsting self')
#     #     self.walk_around()
#     def who_ami(self):
#         print(f'I am {self.name}')
#
#     def get_name(self):
#         return self._name
#
#     def set_name(self, name):
#         if name in ['Barsik, Pushok']:
#             raise Exception('Not available name')
#         self._name = name


# print(cat)
# cat.eat()
# cat.walk_around()
# cat.say_meow()
# print(cat)
# cat.what_is_the_self()

# cat.test_self()

# print(Cat().test_self())

# cat = Cat('grey', 'Alex')
# print(Cat.CATS_CREATED)
# cat2 = Cat('black', 'Georg')
# print(Cat.CATS_CREATED)


# class GlobalVarExampleClass:
#     GLOBAL_VAR_VALUE = 1
#
#     def check_acces_to_class_var(self):
#         return self.GLOBAL_VAR_VALUE
#
#     def set_class_var_value(self, value):
#         self.GLOBAL_VAR_VALUE = value
#
#
# obj = GlobalVarExampleClass()
# print(obj.check_acces_to_class_var())
# obj.set_class_var_value(10)
# print(obj.check_acces_to_class_var())
# print(GlobalVarExampleClass.GLOBAL_VAR_VALUE)


