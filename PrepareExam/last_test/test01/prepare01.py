#!/usr/bin/env python3
import csv
import sys
from datetime import date, datetime

def date_diff(date1,date2):
    try:
        diff = str(datetime.strftime(date1,'%m/%d/%Y')-\
                   datetime.strftime(date2,'%m/%d/%Y')).split()[0]
    except:
        diff = 0
    if diff == '0:00:00':
        diff = 0
    return diff

input_file = sys.argv[1]
output_file = sys.argv[2]

packages = {}
previous_name = 'N/A'
previous_packages = 'N/A'
previous_packages_date = 'N/A'
first_row = True
today = date.today().strftime('%m/%d/%Y')

with open(input_file,'r',newline='') as csv_in_file:
    filereader = csv.reader(csv_in_file)
    header = next(filereader)
    for row in filereader:
        current_name = row[0]
        current_package = row[1]
        current_package_date = row[3]
        if current_name not in packages:
            packages[current_name] = {}
        if current_package not in packages[current_name]:
            packages[current_name][current_package] = 0
        if current_name != previous_name:
            if first_row :
                first_row = False
            else:
                diff = date_diff(today, previous_packages_date)
                if previous_packages in packages[previous_name]:
                    packages[previous_name][previous_packages] = int(diff)
                else :
                    packages[previous_name][previous_packages] += int(diff)
        
