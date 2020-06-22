#!/usr/bin/env/python3
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sns.set(color_codes=True)

#히스토그램
x = np.random.normal(size=1000)
sns.distplot(x,bins=20, kde=False, rug=True, label="histogram")
sns.utils.axlabel("dd")
plt.title("ll")
plt.legend()
plt.show()

#회귀선과 일변량 히스토그램을 포함한 산점도
mean, cov = [5,10],[(1,.5),(.5,1)]
data = np.random.multivariate_normal(mean,cov,200)
data_frame = pd.DataFrame(data, columns=["x","y"])
sns.jointplot(x="x",y="x", data=data_frame, kind="reg").set_axis_labels("x","y")
plt.suptitle("d")
plt.show()

# 쌍별 이변량 산점도
iris = sns.load_dataset("iris")
sns.pairplot(iris)
plt.show()

tips = sns.load_dataset("tips")

#여러 변수에 대한 상자 그림
sns.factorplot(x="time",y="total_bill", hue="smoker", col="day", data=tips, kind="box", size=4, aspect=.5)
plt.show()

#부트스트랩 신뢰구간을 포함한 선형회귀모형
sns.lmplot(x="total_bill", y="tip", data=tips)
plt.show()

#부트스트랩 신뢰구간을 포함한 로지스틱 회귀모형
tips["big_tip"] = (tips.tip/tips.total_bill) > .15
sns.lmplot(x="total_bill", y="big_tip", data=tips, logistic=True,
           y_jitter=.03).set_axis_labels("Total Bill","Big Tip")
plt.title("")
plt.show()