#!/usr/bin/env python3
import csv
import sys

input_file = 'csv/supplier_data_unnecessary_header_footer.csv'
output_file = 'csv/Week05_01.csv'

row_counter = 0
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row in filereader:
            if row_counter >= 3 and row_counter <= 15:
                filewriter.writerow([value.strip() for value in row])
            row_counter+=1