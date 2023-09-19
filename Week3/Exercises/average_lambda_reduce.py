from functools import reduce

my_list = [1, 2, 3]

print(reduce(lambda x, y: x + y, my_list) / len(my_list))
