#!/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

my_columns = ['Invoice Number', 'Purchase Date']
my_columns_index = []

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        for index in range(len(header)):
            if header[index] in my_columns:
                my_columns_index.append(index)
        filewriter.writerow(my_columns)

        for row_list in filereader:
            new_list = []
            for index in my_columns_index:
                new_list.append(row_list[index])
            filewriter.writerow(new_list)