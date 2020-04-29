#!/usr/bin/env python3
import pandas as pd
import sys

input_file = "xls/sales_2013.xlsx"
output_file = "xls/ex02_output.xls"

#입력 파일을 읽어들이고, january_2013 시트를 읽음, index의 칼럼은 없다.
data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

#iloc[행 : 열]
#data_frame에서 전체 행 중에서 1열과 4열을 선택함
data_frame_columns_by_index = data_frame.iloc[:, [1,4]]

writer = pd.ExcelWriter(output_file)
data_frame_columns_by_index.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()