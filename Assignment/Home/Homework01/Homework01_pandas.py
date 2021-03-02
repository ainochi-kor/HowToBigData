#!/usr/bin/env python3
import pandas as pd
import math
input_file = 'supplier_data.csv'
output_file = 'Homework_pandas.csv'

add_df = pd.DataFrame(columns=['Supplier Name','Sum of Cost'])
df = pd.read_csv(input_file)
df['Cost'] = round(df['Cost'].str.strip('$').astype(float))


add_df.loc[1] = ['Supplier X', math.trunc(df.loc[df['Supplier Name'] == 'Supplier X', 'Cost'].sum())]
add_df.loc[2] = ['Supplier Y', math.trunc(df.loc[df['Supplier Name'] == 'Supplier Y', 'Cost'].sum())]
add_df.loc[3] = ['Supplier Z', math.trunc(df.loc[df['Supplier Name'] == 'Supplier Z', 'Cost'].sum())]

add_df.to_csv(output_file, index = False)