#!/usr/bin/env python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
from sklearn.linear_model import LinearRegression

input_file = 'encar_all_info_refine_01.csv'

#폰트설정
font_path="C:/Windows/Fonts/NanumSquareL.ttf"
fontprop = fm.FontProperties(fname=font_path, size=18).get_name()

df = pd.read_csv(input_file)
print(df.describe())

#데이터셋 처음 5개 출력하기
print(df.head())

#print(matplotlib.get_configdir())
plt.rc('font',family=fontprop)
X = df["company"]
y = df["money"]
plt.plot(X,y,'o')
plt.show()

#
# line_fitter = LinearRegression()
# line_fitter.fit(X,y)
#
# y_predicted = line_fitter.predict(X)
