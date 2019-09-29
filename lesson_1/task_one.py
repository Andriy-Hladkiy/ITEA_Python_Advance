my_list = []
n = int(input('Enter number of digit:\n'))

for i in range(0, n+1):
    my_list.append(i)

for i in my_list:
    if i % 2 == 0:
        print(i)
