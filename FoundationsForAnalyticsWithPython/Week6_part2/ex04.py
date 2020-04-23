#!/usr/bin/env python3
import pandas as pd
import sys

input_file = 'xls/sales_2013.xlsx'
output_file = 'xls/ex04_output.xls'

data_frame = pd.read_excel(input_file, 'january_2013', index_col = None)

important_dates = ['01/24/2013', '01/31/2013']
data_frame_value_meets_condition = data_frame[data_frame['Purchase Date'].isin(important_dates)]

writer = pd.ExcelWriter(output_file)
data_frame_value_meets_condition.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()