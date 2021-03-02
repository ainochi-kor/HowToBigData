#!/usr/bin/env python3
import csv
import glob
import os
import string
import sys

input_file = 'supplier_data.csv'
output_file = 'Homework.csv'

head_list = ['Supplier Name', 'Sum of Cost']
name_list = ['Supplier X', 'Supplier Y', 'Supplier Z']

csv_out_file = open(output_file, 'a', newline='')
filewriter = csv.writer(csv_out_file)
filewriter.writerow(head_list)

output_list = []

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        #output_list.append(head_list)
        header = next(filereader)
        x_sales = 0.0
        y_sales = 0.0
        z_sales = 0.0
        for row in filereader:

            select_name = str(row[0]).strip()
            if select_name == name_list[0]:
                x_names = select_name
                amount = row[3]
                x_sales += float(str(amount).strip('$').replace(',',''))

            elif select_name == name_list[1]:
                y_names = select_name
                amount = row[3]
                y_sales += float(str(amount).strip('$').replace(',',''))
            elif select_name == name_list[2]:
                z_names = select_name
                amount = row[3]
                z_sales += float(str(amount).strip('$').replace(',',''))

        # Supplier X sales 넣기
        output_list.append(x_names)
        output_list.append(x_sales)
        filewriter.writerow(output_list)
        output_list = []

        # Supplier Y sales 넣기
        output_list.append(y_names)
        output_list.append(y_sales)
        filewriter.writerow(output_list)
        output_list = []

        # Supplier Z sales 넣기
        output_list.append(z_names)
        output_list.append(z_sales)
        filewriter.writerow(output_list)
    csv_in_file.close()
csv_out_file.close()