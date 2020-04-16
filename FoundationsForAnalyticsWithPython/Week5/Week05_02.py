import pandas as pd
import sys

input_file = 'csv/supplier_data_unnecessary_header_footer.csv'
output_file = 'csv/Week05_02_pandas.csv'

data_frame = pd.read_csv(input_file, header=None)

data_frame = data_frame.drop([0,1,2,16,17,18]) #행을 제거하는 함수 drop
# 밑에 두 문장은 사실 쓸 필요가 없음.
data_frame.columns = data_frame.iloc[0] # 위치 0에 있는 것을 행 즉 헤더로 함.
data_frame = data_frame.reindex(data_frame.index.drop(3)) # 3에 해당하는 행을 뺌.

data_frame.to_csv(output_file, index=False)