# review data COR/REG analysis

'''
[V] 맛/양/배달과 별점 간의 상관관계 및 회귀분석
[V] 주문그룹/브랜드별과 별점 간의 상관분석
'''


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn import linear_model

os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset\2차 분석")
# df = pd.read_excel("Review.xlsx") # 전체 리뷰
df = pd.read_excel("sample.xlsx") # 샘플 테스트
book = pd.read_excel("MENU.xlsx")
cor_df = df.loc[:, ['별점', '맛', '양', '배달']]
'''
# 상관관계 분석

print(round(cor_df.corr(method = 'pearson'), 3))
       별점      맛      양     배달
별점  1.000  0.702  0.601  0.558
맛   0.702  1.000  0.833  0.735
양   0.601  0.833  1.000  0.737
배달  0.558  0.735  0.737  1.000
'''


model = smf.ols(formula = '별점~맛', data = cor_df)
result = model.fit()
print(result.summary())

X_data = df[['맛', '양', '배달']]
Y_data = df['별점']

x_data1 = sm.add_constant(X_data, has_constant = "add")
multi_model = sm.OLS(Y_data, x_data1)
fitted_multi_model = multi_model.fit()
print(fitted_multi_model.summary())

'''
                            OLS Regression Results
==============================================================================
Dep. Variable:                     별점   R-squared:                       0.493
Model:                            OLS   Adj. R-squared:                  0.493
Method:                 Least Squares   F-statistic:                 3.853e+04
Date:                Thu, 18 Feb 2021   Prob (F-statistic):               0.00
Time:                        22:17:22   Log-Likelihood:                -31668.
No. Observations:               39573   AIC:                         6.334e+04
Df Residuals:                   39571   BIC:                         6.336e+04
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      2.1254      0.013    159.678      0.000       2.099       2.151
맛              0.5572      0.003    196.303      0.000       0.552       0.563
==============================================================================
Omnibus:                     8162.440   Durbin-Watson:                   2.005
Prob(Omnibus):                  0.000   Jarque-Bera (JB):           314682.049
Skew:                          -0.049   Prob(JB):                         0.00
Kurtosis:                      16.814   Cond. No.                         24.1
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
                            OLS Regression Results
==============================================================================
Dep. Variable:                     별점   R-squared:                       0.497
Model:                            OLS   Adj. R-squared:                  0.497
Method:                 Least Squares   F-statistic:                 1.304e+04
Date:                Thu, 18 Feb 2021   Prob (F-statistic):               0.00
Time:                        22:17:23   Log-Likelihood:                -31517.
No. Observations:               39573   AIC:                         6.304e+04
Df Residuals:                   39569   BIC:                         6.308e+04
Df Model:                           3
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          2.0405      0.014    142.318      0.000       2.012       2.069
맛              0.4963      0.005     91.852      0.000       0.486       0.507
양              0.0128      0.006      2.320      0.020       0.002       0.024
배달             0.0664      0.004     15.521      0.000       0.058       0.075
==============================================================================
Omnibus:                     8595.455   Durbin-Watson:                   2.004
Prob(Omnibus):                  0.000   Jarque-Bera (JB):           330645.454
Skew:                           0.234   Prob(JB):                         0.00
Kurtosis:                      17.153   Cond. No.                         43.7
==============================================================================
'''

# 주문그룹/브랜드별과 별점 간의 상관분석
cor_df = df.loc[:, ['브랜드명', '그룹구분', '별점']]
model = smf.ols(formula = '별점~브랜드명', data = cor_df)
result = model.fit()
print(result.summary())

model = smf.ols(formula = '별점~그룹구분', data = cor_df)
result = model.fit()
print(result.summary())

'''
                            OLS Regression Results
==============================================================================
Dep. Variable:                     별점   R-squared:                       0.018
Model:                            OLS   Adj. R-squared:                  0.018
Method:                 Least Squares   F-statistic:                     81.51
Date:                Thu, 18 Feb 2021   Prob (F-statistic):          1.13e-150
Time:                        22:42:36   Log-Likelihood:                -44759.
No. Observations:               39573   AIC:                         8.954e+04
Df Residuals:                   39563   BIC:                         8.962e+04
Df Model:                           9
Covariance Type:            nonrobust
====================================================================================
                       coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------------
Intercept            4.8443      0.010    482.918      0.000       4.825       4.864
브랜드명[T.김준현의피자헤븐]    -0.1719      0.021     -8.351      0.000      -0.212      -0.132
브랜드명[T.도미노피자]       -0.2198      0.020    -11.220      0.000      -0.258      -0.181
브랜드명[T.미스터피자]       -0.3060      0.018    -17.385      0.000      -0.341      -0.272
브랜드명[T.반올림피자샵]      -0.0675      0.013     -5.166      0.000      -0.093      -0.042
브랜드명[T.파파존스피자]      -0.2353      0.016    -14.828      0.000      -0.266      -0.204
브랜드명[T.피자나라치킨공주]    -0.2616      0.015    -18.009      0.000      -0.290      -0.233
브랜드명[T.피자마루]        -0.1728      0.029     -5.910      0.000      -0.230      -0.115
브랜드명[T.피자알볼로]       -0.1189      0.015     -8.113      0.000      -0.148      -0.090
브랜드명[T.피자헛]         -0.2635      0.015    -18.125      0.000      -0.292      -0.235
==============================================================================
Omnibus:                    23941.411   Durbin-Watson:                   2.026
Prob(Omnibus):                  0.000   Jarque-Bera (JB):           199734.881
Skew:                          -2.915   Prob(JB):                         0.00
Kurtosis:                      12.335   Cond. No.                         10.0
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
                            OLS Regression Results
==============================================================================
Dep. Variable:                     별점   R-squared:                       0.003
Model:                            OLS   Adj. R-squared:                  0.003
Method:                 Least Squares   F-statistic:                     26.41
Date:                Thu, 18 Feb 2021   Prob (F-statistic):           9.81e-27
Time:                        22:42:36   Log-Likelihood:                -45057.
No. Observations:               39573   AIC:                         9.013e+04
Df Residuals:                   39567   BIC:                         9.018e+04
Df Model:                           5
Covariance Type:            nonrobust
====================================================================================
                       coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------------
Intercept            4.7058      0.026    180.833      0.000       4.655       4.757
그룹구분[T.Large]       -0.0282      0.027     -1.058      0.290      -0.081       0.024
그룹구분[T.Medium]      -0.1052      0.031     -3.407      0.001      -0.166      -0.045
그룹구분[T.Original]    -0.0539      0.038     -1.419      0.156      -0.128       0.021
그룹구분[T.Regular]      0.0540      0.027      1.977      0.048       0.000       0.108
그룹구분[T.Set]         -0.0539      0.027     -1.999      0.046      -0.107      -0.001
==============================================================================
Omnibus:                    24335.742   Durbin-Watson:                   2.024
Prob(Omnibus):                  0.000   Jarque-Bera (JB):           208049.666
Skew:                          -2.969   Prob(JB):                         0.00
Kurtosis:                      12.535   Cond. No.                         19.7
'''