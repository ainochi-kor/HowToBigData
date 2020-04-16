#!/usr/bin/env python3
import pandas as pd
import sys

input_file = 'csv/None_Header.csv'
output_file = 'csv/Week05_04_pandas.csv'

header_list = ['Supplier Name', 'Invoice Number', \
                       'Part Number', 'Cost', 'Purchase Date']
data_frame = pd.read_csv(input_file, header=None, names=header_list)
data_frame.to_csv(output_file, index=False)