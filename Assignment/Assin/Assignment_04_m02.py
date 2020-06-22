#!/usr/bin/env python3

dict = {}
list1 = ['x', 'y', 'z']
list2 = ['a', ['greate', 123], 'd']

for index in range(len(list1)):
    if list1[index] not in dict:
        dict[list1[index]] = list2[index]

for key, value in dict.items():
    print("{0!s}: {1}".format(key, value))



