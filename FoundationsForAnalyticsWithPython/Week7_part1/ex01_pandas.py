#!/usr/bin/env python3
import pandas as pd
import sys

input_file = "xls/sales_2013.xlsx"
output_file = "xls/ex01_pandas_output.xls"

#입력 파일을 읽어들이고, january_2013 시트를 읽음, index의 칼럼은 없다.
data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

#startswith("J") : J를 가지고 시작하는 문자열을 찾음.
#Customer Name의 문자열 중 J로 시작되는 행만 모두 뽑음.
data_frame_value_matches_pattern = data_frame[data_frame['Customer Name'].str.startswith("J")]

writer = pd.ExcelWriter(output_file)
data_frame_value_matches_pattern.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()