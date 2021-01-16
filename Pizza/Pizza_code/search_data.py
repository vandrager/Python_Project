import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")
# brand = ['도미노피자', '피자헛', '미스터피자', '피자스쿨', '피자마루', '파파존스', '피자알볼로', '피자나라치킨공주', '7번가피자', '피자헤븐']

df = round(pd.read_excel("daily_search.xlsx"), 3)
print(df.info())
print(df.describe())
print(df.loc[:, ["도미노피자", "반올림피자샵", "피자나라치킨공주"]].describe())

df['날짜'] = df['날짜'].astype('str') # 문자열 메소드 사용을 위해 자료형 변경
dates = df['날짜'].str.split('-') # 문자열을 split 메소드로 분리
# print(dates.head())
df['연'] = dates.str.get(0)
df['월'] = dates.str.get(1)
df['일'] = dates.str.get(2)

print(df.head())
df.to_csv("search_data.csv", encoding = "cp949")