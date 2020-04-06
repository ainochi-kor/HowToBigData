#!/usr/bin/env/ python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

#read_csv는 입력으로 온 csv파일을 테이블 모양의 데이터 프레임을 만든다.
data_frame = pd.read_csv(input_file)

important_dates = ['1/20/14', '1/30/14']
#loc는 데이터 프레임 안에 있는 값을 해당 데이터를 찾아준다.
data_frame_value_in_set = data_frame.loc[data_frame['Purchase Date']\
    .isin(important_dates), :]

data_frame_value_in_set.to_csv(output_file, index=False)

#python Week4_02.py csv/Supplier_data.csv csv/Week4_02.csv