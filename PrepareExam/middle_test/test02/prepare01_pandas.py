#!/usr/bin/env python3
import pandas as pd
import os
import sys
import glob

input_path = sys.argv[1]
output_file = sys.argv[2]

all_files = glob.glob(os.path.join(input_path,'sales_*'))

all_df = []
for file in all_files:
    df = pd.read_csv(file)
    all_df.append(df)

all_df_concat = pd.concat(all_df, axis=0, ignore_index=False)
all_df_concat.to_csv(output_file, index=False)