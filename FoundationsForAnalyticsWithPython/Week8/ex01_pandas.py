#!/usr/bin/env python3
import pandas as pd
#import sys

input_file = 'xls/sales_2013.xlsx'
output_file = 'xls/ex01_pandas_output.xls'
#sheet_name=None은 sheet_name을 지정하지 않으므로 모든 워크시트를 읽어들인다.
data_frame = pd.read_excel(input_file, sheet_name=None, index_col=None)
'''
이때 읽은 워크시트는 key 값하고 값들로 구성되는 dictionary 구조로 구성된다.
'''
row_output = [] #출력을 위한 list
#data_frame의 아이템들을 가지고 for문을 돌림.
for worksheet_name, data in data_frame.items():
    #Sale Amount의 $와 ,를 없애고 그 값은 2000을 이상의 값을 append한다.
    row_output.append(data[data['Sale Amount'].replace('$', '').replace(',', '').astype(float) > 2000.0])
#전체를 하나로 묶어줌. 행은 아래로 붙여 나감.
filtered_rows = pd.concat(row_output, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name = 'sale_amount_gt2000',index=False)
writer.save()
