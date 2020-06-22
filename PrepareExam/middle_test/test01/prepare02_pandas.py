#!/usr/bin/env python3

import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

df = pd.read_csv(input_file)
new_df = df.loc[:,['Invoice Number','Purchase Date']]

new_df.to_csv(output_file,index=False)