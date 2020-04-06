#!/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

my_columns = [0, 3]

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row_list in filereader:
            row_list_output = [] #my_colums의 각 해당 값만 뽑아서 리스트를 저장하기 위함.
            for index_value in my_columns: # indes_value 에서 0, 3에 해당되는 값을 index_value에 담음.
                row_list_output.append(row_list[index_value]) # 현재 index_value 값을 추가함.
            filewriter.writerow(row_list_output)

#python Week4_05.py csv/Supplier_data.csv csv/Week4_05.csv