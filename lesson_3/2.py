# def mult(obj):
#     return obj * 2
#
#
# print(mult(100))
#
# a = lambda obj: obj * 2
#
# print(a(100))

#############################################################

# list_of_values = [1, 2, 4, 5, 6, ]
#
# print(list(map(lambda value: value * 2, list_of_values)))
#
list_of_values = [1, 2, 4, 5, 6, ]

print(list(filter(lambda value: value % 2 == 0, list_of_values)))
