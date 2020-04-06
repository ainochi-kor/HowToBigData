#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
#.ix 는 index를 의미함.
#데이터 프레임에서 invoice number에 해당하는 문자열의 001-패턴의 행을 추출.
data_frame_value_matches_pattern = data_frame.ix[data_frame['Invoice Number'].str.startswith("001-"), :]
data_frame_value_matches_pattern.to_csv(output_file, index=False)

#python Week4_04.py csv/Supplier_data.csv csv/Week4_04.csv