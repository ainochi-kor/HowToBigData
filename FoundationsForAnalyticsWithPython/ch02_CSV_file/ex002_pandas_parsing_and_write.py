#!/usr/bin/env python3
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

#panda를 통해 읽은 csv파일을 data_frame 변수에 저장한다.
data_frame = pd.read_csv(input_file)
#data_frame을 출력한다.
print(data_frame)
#data_frame이라는 변수 안에 있는 데이터프레임을 csv형태로 저장한다.
data_frame.to_csv(output_file, index=False)
