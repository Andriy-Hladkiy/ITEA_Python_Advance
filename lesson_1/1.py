# list_var = [1, 2, 3, 'a', 'b']
#
# list_var.append([1, 2, 3, 4])
# list_var.extend([1, 2, 3])
# list_var.insert(0, 'New element')
# list_var.pop(0)
# #list_var.clear()
# #list_var.remove()
# del list_var[2]
#
# print(list_var)
#
#
# dict_var_1 = dict(
#     key='value',
#     new_ley='new_value'
# )
#
# print(dict_var_1['key'])
#
#
# set_var = {1, 2, 3, 'a', 'b', 'b'}
#
# print(set_var)
#
#
# time = 12
#
# print('goood morning') if time < 13 else print('Hello')
#
#
# # list_var = [1, 2, 3]
#
# # for i in enumerate(list_var):
# # print(i)
#
# # for i in range(0, 100):
# # print(i)
#
# # a = 0
# # while a < 10:
# #   print(a)
# #    a += 1
#
#
# my_str = 'aaa'
#
# try:
#     1 / 0
#     my_str[2] = 'N'
# except (ZeroDivisionError, TypeError) as e:
#     print(e)
#     print('Zero division not allowed')
#
# finally:
#     print('Try except block ennded')


def say_meow():
    print('MEOW')


def doubler(arg):
    return arg * 2


doubler_value = doubler(10)
print(doubler_value)
