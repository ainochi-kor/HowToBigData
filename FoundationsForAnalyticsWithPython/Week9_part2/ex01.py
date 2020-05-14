#!/usr/bin/env python3
import glob
import os
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_folder = 'xls'
output_file = 'output/ex01_output.xls'

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('sums_and_averages')

all_data = [] #최종 데이터
sales_column_index = 3 #sales_amount 위치를 가리킴.

#출력에 사용할 헤더의 이름
header = ['workbook', 'worksheet', 'worksheet_total', 'worksheet_average', \
          'workbook_total', 'workbook_average']
all_data.append(header) #헤더를 추가함.

#for문은 통합문서만큼 돌게 된다.
for input_file in glob.glob(os.path.join(input_folder, '*.xls*')):
    with open_workbook(input_file) as workbook: #엑셀파일을 열다.
        list_of_totals = []
        list_of_numbers = []
        workbook_output = []
        print(list_of_totals)
        for worksheet in workbook.sheets():
            total_sales = 0 # 워크시트 안의 토탈.
            number_of_sales = 0 # 평균을 구하기 위한 변수
            worksheet_list = []
            worksheet_list.append(os.path.basename(input_file)) #input_file의 이름
            worksheet_list.append(worksheet.name) #worksheet의 이름
            for row_index in range(1,worksheet.nrows): # row갯수만큼
                try:
                    total_sales += float(str(worksheet.cell_value(row_index, sales_column_index)).strip('$').replace(',',''))
                    number_of_sales += 1.
                except:
                    total_sales += 0.
                    number_of_sales += 0.
            #평균을 구하는 변수
            average_sales = '%.2f'%(total_sales/number_of_sales)
            worksheet_list.append(total_sales)
            worksheet_list.append(float(average_sales))
            list_of_totals.append(total_sales)
            list_of_numbers.append(float(number_of_sales))
            workbook_output.append(worksheet_list)
        workbook_total = sum(list_of_totals)
        workbook_average = sum(list_of_totals)/sum(list_of_numbers)
        for list_element in workbook_output:
            list_element.append(workbook_total)
            list_element.append(workbook_average)
        all_data.extend(workbook_output)

for list_index, output_list in enumerate(all_data):
    for element_index, element in enumerate(output_list):
        output_worksheet.write(list_index,element_index,element)

output_workbook.save(output_file)