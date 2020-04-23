#!/usr/bin/env python3
import sys
from xlrd import open_workbook

input_file = 'xls/sales_2013.xlsx'

workbook = open_workbook(input_file)
print('Number of worksheets: ',workbook.nsheets)
for worksheet in workbook.sheets():
    print("Worksheet name:", worksheet.name, "\tRow:", worksheet.nrows, "\tColumns:", worksheet.ncols)