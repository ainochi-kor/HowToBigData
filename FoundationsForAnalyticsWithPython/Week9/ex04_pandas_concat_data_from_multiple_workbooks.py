#!/usr/bin/env python3
import pandas as pd
import glob
import os
import sys

input_path = 'xls'
output_file = 'output/ex04_pandas_output.xls'

all_workbooks = glob.glob(os.path.join(input_path,'*.xls*'))
data_frames = []
#엑셀 파일에 대해서.
for workbook in all_workbooks:
    all_worksheets = pd.read_excel(workbook, sheet_name=None, index_col=None)
    for worksheet_name, data in all_worksheets.items():
        data_frames.append(data)
all_data_concatenated = pd.concat(data_frames, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
all_data_concatenated.to_excel(writer, sheet_name='all_data_workbooks', index=False)
writer.save()