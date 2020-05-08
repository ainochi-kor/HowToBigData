#!/usr/bin/env python3
import pandas as pd
#import sys

input_file = 'xls/sales_2013.xlsx'
output_file = 'xls/ex02_pandas_output.xls'

#딕셔너리 자료구조를 가짐.
data_frame = pd.read_excel(input_file, sheet_name=None, index_col=None)

columns_output = []
for worksheet_name, data in data_frame.items():
    #2개의 열에 대해서 모든 행을 추가함.
    columns_output.append(data.loc[:, ['Customer Name', 'Sale Amount']])
#출력된 값을 붙임
selected_columns = pd.concat(columns_output, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
selected_columns.to_excel(writer, sheet_name='selected_columns_all_worksheets', index=False)
writer.save()