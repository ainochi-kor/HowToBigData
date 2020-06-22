#!/usr/bin/env python3
import os
import sys
import glob
import pandas as pd

input_path = sys.argv[1]
output_file = sys.argv[2]

all_workbooks = glob.glob(os.path.join(input_path,'*.xlsx'))
df = []
for workbook in all_workbooks:
    all_worksheets = pd.read_excel(workbook, sheet_name=None, index_cel=False)
    for sheet_name, data in all_worksheets.items():
        df.append(data)

concat_df = pd.concat(df, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
concat_df.to_excel(writer, sheet_name="add_sheet", index=False)
writer.save()