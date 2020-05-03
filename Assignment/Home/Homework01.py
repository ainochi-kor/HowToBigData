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

with open(input_file, 'r', newline='') as csv_in_file:
    filereader = csv.reader(csv_in_file)
    output_list = []
    output_list.append(head_list)
    header = next(filereader)
    x_sum = 0.0
    y_sum = 0.0
    z_sum = 0.0
    for row in filereader:
        amount = row[3]
        name = row[0]
        if name == name_list[0]:
            x_sum += float(str(amount).strip('$').replace(',', ''))
        elif name == name_list[1]:
            y_sum += float(str(amount).strip('$').replace(',', ''))
        elif name == name_list[2]:
            z_sum += float(str(amount).strip('$').replace(',', ''))
    for row in filereader:
        sale_amount = row[3]
        total_sales += float(str(sale_amount).strip('$').replace(',',''))
        number_of_sales += 1.0
    average_sales = '{0:.2f}'.format(total_sales/number_of_sales)
    output_list.append(total_sales)
    output_list.append(average_sales)
    filewriter.writerow(output_list)
csv_out_file.close()







# with open(input_file, 'r', newline='') as csv_in_file:
# with open(output_file, 'w', newline='') as csv_out_file:
#     filereader = csv.reader(csv_in_file)
#     filewriter = csv.writer(csv_out_file)
#     header = next(filereader)
#     x_sum = 0.0
#     y_sum = 0.0
#     z_sum = 0.0
#     for row in filereader:
#         amount = row[3]
#         name = row[0]
#         if name == name_list[0]:
#             x_sum += float(str(amount).strip('$').replace(',', ''))
#         elif name == name_list[1]:
#             y_sum += float(str(amount).strip('$').replace(',', ''))
#         elif name == name_list[2]:
#             z_sum += float(str(amount).strip('$').replace(',', ''))
#     data = {name_list[0]: x_sum,
#             name_list[1]: y_sum,
#             name_list[2]: z_sum}
#     filewriter.writerow(head_list)
#     filewriter.writerow(head_list)
