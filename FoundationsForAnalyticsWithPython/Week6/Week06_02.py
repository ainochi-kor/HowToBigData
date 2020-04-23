#!/usr/bin/env python3

import sys
from xlrd import open_workbook
from xlwt import Workbook

input_file = 'xls/sales_2013.xlsx'
output_file = 'xls/Week06_02_output.xls'

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    for row_index in range(worksheet.nrows):
        for columns_index in range(worksheet.ncols):
            output_worksheet.write(row_index, columns_index, worksheet.cell_value(row_index, columns_index))
output_workbook.save(output_file)