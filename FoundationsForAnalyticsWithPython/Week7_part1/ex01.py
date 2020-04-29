#!/usr/bin/env python3
import re #패턴 매칭을 위해 필요한 모듈
import sys
from datetime import date #날짜처리를 위한 모듈
from xlrd import open_workbook, xldate_as_tuple #엑셀의 통합문서를 처리하기 위한 모듈
from xlwt import Workbook #엑셀의 통합문서를 처리하기 위한 모듈

input_file = 'xls/sales_2013.xlsx'
output_file = 'xls/ex01_output.xls'

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output') #시트를 하나 추가시킴.

pattern = re.compile(r'(?P<my_pattern>^J.*)') #패턴을 정의함. "대문자 J로 시작하는 문자열"을 찾는 패턴.

customer_name_column_index = 1 #패턴 매칭시 B열인 index[1]열이 필요함.
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013') #워크시트 중 'january_2013'만 이용용
    data = []
    header = worksheet.row_values(0) #0인 로우(헤더)를 헤더에 저장
    data.append(header) #빈 리스트에 헤드를 추가함.
    for row_index in range(1, worksheet.nrows): #1부터 시작해서  nrow(마지막 행)까지.
        row_list = [] #빈 row_list를 정의
        if pattern.search(worksheet.cell_value(row_index, customer_name_column_index)): #(1,1)의 값을 패턴 매칭을 함.
            for column_index in range(worksheet.ncols) : # 0~4까지의 칼럼 범위
                cell_value = worksheet.cell_value(row_index, column_index)
                #print(row_index, column_index)
                cell_type = worksheet.cell_type(row_index, column_index)
                if cell_type == 3:
                    date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                    date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y') #날짜 타입을 변경함.
                    row_list.append(date_cell)
                else:
                    row_list.append(cell_value)
        if row_list:
            data.append(row_list)
    #값들을 붙여 나가는 과정.
    for list_index, output_list in enumerate(data):
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)