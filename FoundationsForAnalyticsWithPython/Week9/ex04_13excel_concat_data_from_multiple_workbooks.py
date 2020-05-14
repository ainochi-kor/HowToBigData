#!/usr/bin/env python3
import glob
import os
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_folder = 'xls'
output_file = 'output/ex04_output.xls'

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('all_data_all_workbooks')

data = []
first_worksheet = True
#입력 주소에서 파일을 읽기
for input_file in glob.glob(os.path.join(input_folder, '*.xls*')):
    print(os.path.basename(input_file)) #무엇을 읽었는지 출력
    with open_workbook(input_file) as workbook:
        for worksheet in workbook.sheets(): #모든 워크시트
            if first_worksheet:
                header_row = worksheet.row_values(0)
                data.append(header_row)
                first_worksheet = False
            for row_index in range(1, worksheet.nrows):
                row_list = []
                for column_index in range(worksheet.ncols):
                    cell_value = worksheet.cell_value(row_index, column_index)
                    cell_type = worksheet.cell_type(row_index, column_index)
                    if cell_type == 3:
                        date_cell = xldate_as_tuple(cell_value,workbook.datemode)
                        date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                        row_list.append(date_cell)
                    else:
                        row_list.append(cell_value)
                data.append(row_list)

for list_index, output_list in enumerate(data):
    for element_index, element in enumerate(output_list):
        output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)