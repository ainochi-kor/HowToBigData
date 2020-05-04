#!/usr/bin/env python
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

#data_frame에 input_file을 pd를 이용하여 read_csv한다.
data_frame = pd.read_csv(input_file)

#Cost 열에 $표시를 제거하고, float형태로 만든다.
data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)
data_frame_value_meets_condition = data_frame.loc[(data_frame['Supplier Name'].str.contains('Z'))\
                                                  | (data_frame['Cost'] > 600.0), :]
data_frame_value_meets_condition.to_csv(output_file, index=False)