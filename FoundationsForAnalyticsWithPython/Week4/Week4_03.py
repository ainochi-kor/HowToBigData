#!/usr/bin/env python3
import csv
import re
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

#정규 표현식. 001- 으로 시작하는 패턴을 찾는 것.
pattern = re.compile(r'(?P<my_pattern_group>^001-.*)', re.I)

with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader) #첫번째 줄을 읽는다. 즉 Head를 읽음.
        for row_list in filereader:
            invoice_number = row_list[1] #2번째 열의 값을 대입.
            if pattern.search(invoice_number): #001로 시작하는 문자열을 찾음.
                filewriter.writerow(row_list)

#python Week4_03.py csv/Supplier_data.csv csv/Week4_03.csv

