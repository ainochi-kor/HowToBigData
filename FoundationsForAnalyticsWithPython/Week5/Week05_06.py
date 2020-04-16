#!ust/bin/env python3
import pandas as pd
import glob
import os
import sys

input_path = 'csv'
output_file = 'csv/Week05_06_pandas.csv'

all_files = glob.glob(os.path.join(input_path,'sales_*'))

all_data_files = [] #3개의 데이터를 모을 것.
for file in all_files: #3개의 파일을 읽어드림.
    data_frame = pd.read_csv(file, index_col = None)
    all_data_files.append(data_frame)
#세개의 파일을 모두 붙여버리는 역할
# 0 아래로 붙임 1 옆으로 붙임.
data_frame_concat = pd.concat(all_data_files, axis=0, ignore_index=True)

data_frame_concat.to_csv(output_file, index = False)