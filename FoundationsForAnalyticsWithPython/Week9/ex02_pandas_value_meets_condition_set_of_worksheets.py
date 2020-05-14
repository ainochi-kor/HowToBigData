#!/usr/bin/env python3
import pandas as pd
import sys

input_file = 'xls/sales_2013.xlsx'
output_file = 'output/ex02_output.xls'

my_sheets = [0, 1] #sheet
threshold = 1900.0 #기준 값.

data_frame = pd.read_excel(input_file, sheet_name=my_sheets, index_col=None)

row_list = []
for worksheet_name, data in data_frame.items():
    row_list.append(data[data['Sale Amount'].astype(float) > threshold])
filter_rows = pd.concat(row_list, axis=0, ignore_index=True)
writer = pd.ExcelWriter(output_file)
filter_rows.to_excel(writer, sheet_name='set_of_worksheets', index=False)
writer.save()