#!/usr/bin/env python3
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = 'xls/sales_2013.xlsx'
output_file = 'output/ex01_output.xls'

output_workbook = Workbook()
#출력시 결과로 나오는 sheet의 이름.
output_worksheet = output_workbook.add_sheet('set_of_worksheets')

my_sheets = [0,1] #sheet 지정
threhold = 1900.0 #기준 값을 지정
sales_column_index = 3 #Sales_amount를 가리키기 위한 index번호

first_worksheet = True
with open_workbook(input_file) as workbook:
    data = []
    for sheet_index in range(workbook.nsheets):
        if sheet_index in my_sheets: #sheet가 0 or 1인지 확인.
            worksheet = workbook.sheet_by_index(sheet_index)
            if first_worksheet:
                header_row = worksheet.row_values(0) #헤더를 뽑음
                data.append(header_row) #데이터에 헤더를 추가함.
                first_worksheet = False #헤더를 다시 뽑지 않도록 False로 함.
            for row_index in range(1,worksheet.nrows): #행의 1번 즉, 헤더 빼고 시작함.
                row_list = []
                sale_amount = worksheet.cell_value(row_index,sales_column_index)
                if sale_amount > threhold: #salse_amount가 1900보다 크면 True.
                    for column_index in range(worksheet.ncols):
                        cell_value = worksheet.cell_value(row_index,column_index)
                        cell_type = worksheet.cell_type(row_index, column_index)
                        if cell_type == 3: #날짜 타입이면 Ture
                            date_cell = xldate_as_tuple(cell_value,workbook.datemode)
                            date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                            row_list.append(date_cell)
                        else:
                            row_list.append(cell_value)
                if row_list:
                    data.append(row_list)

    for list_index, output_list in enumerate(data):
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)