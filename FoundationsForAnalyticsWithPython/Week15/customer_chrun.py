#!/usr/bin/env python3
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

# 데이터셋을 데이터 프레임으로 읽음.
churn = pd.read_csv('churn.csv', sep=',', header=0)

churn.columns = [heading.lower() for heading in \
                 churn.columns.str.replace(' ','_').str.replace("\'","").str.strip('?')]

churn['churn'] = np.where(churn['churn'] == 'True.',1.,0.)
print(churn.head())



#그룹별 기술통계 구하기
print(churn.groupby(['churn'])[['day_charge', 'eve_charge', 'night_charge', \
                                'intl_charge', 'account_length', 'custserv_calls']].agg(['count', 'mean','std']))
# 변수별로 서로 다른 통계랑 구하기
print(churn.groupby(['churn']).agg({'day_charge' : ['mean','std'],
                                    'eve_charge' : ['mean','std'],
                                    'night_charge' : ['mean','std'],
                                    'intl_charge' : ['mean','std'],
                                    'account_length' : ['count', 'min', 'max'],
                                    'custserv_calls' : ['count', 'min', 'max']}))

# 새로운 변수 total_charges를 기준으로 그룹화 한 뒤,
# 그룹별 통계량 구하기
churn['total_charges'] = churn['day_charge']+churn['eve_charge'] +\
    churn['night_charge'] + churn['intl_charge']
factor_cut = pd.cut(churn.total_charges, 5, precision=2) #전체 요금을 5구간으로 나누고 정밀도는 2.
def get_stats(group):
    return {'min' : group.min(),'max' : group.max(),
            'count' : group.count(), 'mean' : group.mean(),
            'std' : group.std()}
grouped = churn.custserv_calls.groupby(factor_cut)
print(grouped.apply(get_stats).unstack())

# account_length 열의 사분위수를 기준으로 분할한 뒤,
# 그룹별 통계랑 구하기
factor_qcut = pd.qcut(churn.account_length,[0., 0.25, 0.5, 0.75, 1.])
grouped = churn.custserv_calls.groupby(factor_qcut)
print(grouped.apply(get_stats).unstack)

# intl_plan 와 vmail_plan 열에 대한 이진형 지시변수를 만들고,
# churn 열과 병합하여 새로운 데이터프레임을 생성하기
intl_dummies = pd.get_dummies(churn['intl_plan'], prefix='intl_plan')
vmail_dummies = pd.get_dummies(churn['vmail_plan'], prefix='vmail_plan')
churn_with_dummies = churn[['churn']].join([intl_dummies, vmail_dummies])
print(churn_with_dummies)

# total_charges를 사분위수로 분할하고, 이진형 지시변수를 만들고,
# 새로운 더비변수를 churn 데이터프레임에 추가하기
qcut_names = ['1st_quartile', '2nd_quartile', '3rd_quartile', '4th_quartile']
total_charges_quartiles = pd.qcut(churn.total_charges, 4, labels=qcut_names)
dummies = pd.get_dummies(total_charges_quartiles, prefix='total_charges')
churn_with_dummies = churn.join(dummies)
print(churn_with_dummies.head())

# 피벗 테이블 생성하기
print(churn.pivot_table(['total_charges'], index=['churn','custserv_calls']))
print(churn.pivot_table(['total_charges'], index=['churn'], columns=['custserv_calls']))
print(churn.pivot_table(['total_charges'], index=['custserv_calls'],
                        columns=['churn'], aggfunc='mean', fill_value='NaN', margins=True))

dependent_variable = churn['churn01']
independent_variables = churn[['account_length', 'custserv_calls', 'total_charges']]
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit()

print(logit_model.summary())
print("\nQuantities you can extract from the result:\n%s" % dir(logit_model))
print("\nCoefficients:\n%s" % logit_model.params)
print("\nCoeffcient Std Errors:\n%s" % logit_model.bse)

#로지스틱 회귀모델
def inverse_logit(model_formula):
    from math import exp
    return (1.0 / (1.0 + exp(-model_formula))) * 100.0

at_means = float(logit_model.params[0]) + \
    float(logit_model.params[1])*float(churn['account_length'].mean()) + \
    float(logit_model.params[2])*float(churn['custserv_calls'].mean()) + \
    float(logit_model.params[3])*float(churn['total_charges'].mean())

print(churn['account_length'].mean())
print(churn['custserv_calls'].mean())
print(churn['total_charges'].mean())
print(at_means)
print("P of churn when ind. vars are their mean: %.3f" % inverse_logit(at_means))