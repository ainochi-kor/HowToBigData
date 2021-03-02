#!/usr/bin/env python3
# CSV 파일 작성하기
import pandas as pd

sum_list = [['1','2','3','4','5'],['a', 'b', 'c', 'd', 'e']]
for list1 in sum_list:
    max_index = len(list1)
    output = ''
    for index in range(len(list1)):
        if index < (max_index-1):
            output += str(list1[index])+','
        else :
            output += str(list1[index]) + '\n'
    print(output)





