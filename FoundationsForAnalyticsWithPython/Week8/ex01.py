#/usr/bin/env python3
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = 'xls/sales_2013.xlsx'
output_file = 'xls/ex01_output.xls'

output_workbook = Workbook()
#추가할 워크시트의 이름 : 'filtered_row_all_worksheets'
output_worksheet = output_workbook.add_sheet('filtered_row_all_worksheets')

#3 sales가 있는 칼럼의 index가 [3]이기 때문.
sales_column_index = 3
#slaes amount에서 2000보다 더 큰 값을 찾기 위해 임계값을 준 것.
threshold = 2000.0

#첫번째 워크시트 = 참 // 헤더만 뽑아서 변수에서 할당하기 위함.
first_worksheet = True
#파일 오픈
with open_workbook(input_file) as workbook:
    data = [] #출력하고자 하는 데이터를 모두 모으는 빈 리시트
    for worksheet in workbook.sheets(): #모든 워크시트에 대해서를 의미.
        if first_worksheet:
            header_row = worksheet.row_values(0) #헤더를 header_row 변수에 저장.
            data.append(header_row) #data의 index[0]에 추가함.
            first_worksheet = False #헤더를 만들었으므로 False로 취급
        for row_index in range(1,worksheet.nrows): #1번 행부터 마지막 행까지 돌 것.
            row_list = []
            #워크시트의 sale_amount열의 row_index번째 행의 값을 sale_amount변수에 저장함.
            sale_amount = worksheet.cell_value(row_index, sales_column_index)
            #sale_amount의 형식을 float으로 바꾸고, '$'와 ','를 제거한다.
            sale_amount = float(str(sale_amount).replace('$', '').replace(',', ''))
            #sale_amount가 2000이 넘는지 확인한다.
            if sale_amount > threshold:
                #행에 있는 모든 값을 row_list에 추가하는 과정.
                for column_index in range(worksheet.ncols):
                    cell_value = worksheet.cell_value(row_index, column_index)
                    cell_type = worksheet.cell_type(row_index, column_index)
                    if cell_type == 3: #날짜 형식을 바꿈.
                        date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                        date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                        row_list.append(date_cell)
                    else:
                        row_list.append(cell_value)
            if row_list: #row_list의 값이 있는지 확인.
                data.append(row_list)

    for list_index, output_list in enumerate(data):
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index,element)

output_workbook.save(output_file)