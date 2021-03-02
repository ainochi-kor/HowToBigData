#!ust/bin/env python3
import pandas as pd
import glob
import os
import sys
import math

input_path = 'csv'
output_file = 'csv/Homework02_pandas_output.csv'

all_files = glob.glob(os.path.join(input_path,'sales_*'))

all_data_files = []
for file in all_files:
    data_frame = pd.read_csv(file, index_col = None)
    all_data_files.append(data_frame)

data_frame_concat = pd.concat(all_data_files, axis=0, ignore_index=True)
data_frame_concat["Sale Amount"] = pd.to_numeric(data_frame_concat["Sale Amount"].str.strip('$').replace(',', '',regex=True))

df = pd.DataFrame([['Sale Amount 합계 : ', math.trunc(data_frame_concat["Sale Amount"].sum())]])
df = df.append(pd.DataFrame([['Sale Amount 평균 : ', math.trunc(data_frame_concat["Sale Amount"].mean())]]), ignore_index=True)

data_frame_concat.to_csv(output_file, index = False)
df.to_csv(output_file, mode='a', index=False, header=False)