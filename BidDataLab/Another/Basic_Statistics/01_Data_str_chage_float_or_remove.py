#!/usr/bin/env python3
import pandas as pd
import numpy as np


input_file = 'encar_all_info_crawling3.csv'
output_file = 'encar_all_info_refine_01.csv'

arr = []
df = pd.read_csv(input_file, encoding='cp949')

for i in range(0, len(df)):
    if df["money"][i] == "리스승계":
        arr.append(i)
    else :
        df["money"][i] = float(str(df["money"][i]).strip('$').replace(',', ''))
        print(df["money"][i])

#print(arr)

for i in range(0,len(arr)):
    #print(df.iloc[[arr[i]-i], 4:10])
    df.drop(arr[i],inplace=True)
print(df["money"])

df.to_csv(output_file,index=False)

