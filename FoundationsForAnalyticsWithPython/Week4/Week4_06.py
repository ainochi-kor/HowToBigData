#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
#iloc [ 행 , 열 ]
#.iloc[:, [0, 3]] 는 전체 행과 0,3 열의 index를 의미함.
data_frame_column_by_index = data_frame.iloc[:, [0, 3]]
data_frame_column_by_index.to_csv(output_file, index=False)

#python Week4_06.py csv/Supplier_data.csv csv/Week4_06.csv