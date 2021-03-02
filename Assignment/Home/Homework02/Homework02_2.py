#!ust/bin/env python3
import csv
import glob
import os
import sys
import math

input_path = 'csv'
output_file = 'csv/Homework02_output.csv'

all_csv = []
first_file = True
count, sum = 0.0, 0.0

for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    with open(input_file, 'r', newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        if first_file:
            for row in filereader:
                if row[3] != 'Sale Amount':
                    row[3] = float(str(row[3]).strip('$').replace(',', ''))
                    sum += row[3]
                    count += 1
                all_csv.append(row)
            first_file = False
        else:
            header = next(filereader)
            for row in filereader:
                row[3] = float(str(row[3]).strip('$').replace(',', ''))
                sum += row[3]
                count += 1
                all_csv.append(row)
all_csv.append(['Sales Amount 합계: ',sum])
all_csv.append(['Sales Amount 평균:' , round(sum/count,2)])
print(sum)
print(count)

with open(output_file,'w', newline='', encoding='utf-8') as csv_out_file:
    writer = csv.writer(csv_out_file)
    for index in range(len(all_csv)):
        writer.writerow(all_csv[index])


