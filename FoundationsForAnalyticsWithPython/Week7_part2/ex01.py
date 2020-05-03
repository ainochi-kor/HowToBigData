import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = 'xls/sales_2013.xlsx'
output_file = 'xls/ex01_output.xls'

output_workbook = Workbook() #출력할 때 사용할 통합문서 객체
output_worksheet = output_workbook.add_sheet('jan_2013_output') #워크시트를 하나 만듬.

my_columns = ['Customer Id', 'Purchase Date'] #고객의 ID와 구매날짜만 추출하기 위함.

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013') #'january_2013'워크시트만 봄.
    data = [my_columns] #Customer ID, Purchase Date가  처리가 됨.
    header_list = worksheet.row_values(0) #0번째 행을 저장함
    header_index_list = [] # 여기에 우리가 필요로하는 두 개의 인덱스가 들어갈 것.
    '''
            header_list의 값이 my_columns에 있는가? 
            있으면 그 값을 저장함.
    '''
    for header_index in range(len(header_list)):
        if header_list[header_index] in my_columns:
            header_index_list.append(header_index)
    '''
    row를 증가시키면서 id와 date의 값을 추가해 나감.
    '''
    for row_index in range(1,worksheet.nrows):
        row_list = []
        for column_index in header_index_list:
            cell_value = worksheet.cell_value(row_index, column_index)
            cell_type = worksheet.cell_type(row_index, column_index)
            if cell_type == 3: #날짜 형식이면 3이 나온다고 함.
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