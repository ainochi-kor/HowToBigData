#!/usr/bin/env python3

import csv
import sys

# input_file = sys.argv[0]
# output_file = sys.argv[1]
input_file = 'supplier_data.csv'
output_file = 'prepare01.csv'

my_columns = [0,3]

with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row_list in filereader:
            new_list = []
            for index in my_columns:
                new_list.append(row_list[index])
            filewriter.writerow(new_list)