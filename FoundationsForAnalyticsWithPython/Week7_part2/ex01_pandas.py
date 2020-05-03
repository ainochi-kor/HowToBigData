#!/usr/bin/env python3
import pandas as pd
import sys

input_file = 'xls/sales_2013.xlsx'
output_file = 'xls/ex01_pandas.xls'

#input_file 안의 january_2013 워크시트를 읽는다. 단, col의 index는 없다 (col에 헤더 없음)
#data_frame은 표 형식을 가진다.
data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

#loc는 data_frame안에 해당 값을 찾아줌.
data_frame_columns_by_name = data_frame.loc[:,['Customer Id', 'Purchase Date']]

#출력을 하기 위한 엑셀 통합문서 형식의 writer를 생성
writer = pd.ExcelWriter(output_file)
#writer에 jan_13_output이라는 시트에 추가.
data_frame_columns_by_name.to_excel(writer,sheet_name='jan_13_output', index=False)
#save를 이용하여 출력.
writer.save()