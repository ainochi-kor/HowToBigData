#!/usr/bin/env python3
'''
필요한 데이터만 뽑아내는 것
'''
#import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = 'xls/sales_2013.xlsx'
output_file = 'xls/ex02_output.xls'

output_workbook = Workbook()
#출력을 위한 Sheet Name을 정함.
output_worksheet = output_workbook.add_sheet('selected_columns_all_worksheets')

#두개의 열만 뽑기 위한 데이터.
my_columns = ['Customer Name', 'Sale Amount']

first_worksheet = True #헤더를 뽑기 위한 것.
with open_workbook(input_file) as workbook:
    data = [my_columns] #hader를 추가함.
    index_of_cols_to_keep = [] #추출하려는 index의 값을 넣을 것.
    for worksheet in workbook.sheets(): #모든 워크 시트 확인
        if first_worksheet: #첫번째 워크시트이면
            header = worksheet.row_values(0) #첫번째 행을 헤더에 넣음.
            for column_index in range(len(header)):
                if header[column_index] in my_columns:
                    #my_columns안의 두 열에 대한 값을 추가함.
                    index_of_cols_to_keep.append(column_index)
            first_worksheet = False
        for row_index in range(1,worksheet.nrows):
            row_list = []
            for column_index in index_of_cols_to_keep:
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