import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import matplotlib as mat
import seaborn as sns
mat.rcParams['font.family'] = 'Black Han Sans'
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")
# brand = ['피자헛', '파파존스', '도미노피자', '반올림피자샵', '미스터피자', '피자마루', '피자알볼로', '피자나라치킨공주', '7번가피자', '피자헤븐']

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

# 월 데이터 테스트
test = df[(df['월'] == '01') | (df['월'] == '06')]
print(test)
print(test.info())

## 월별 히트맵 그리기
month_group = df.groupby(['월'])
for key, group in month_group:
    print("* key :", key)
    print("* number :", len(group))
    print(round(group.mean(), 3))
    print('\n')

month = list(set(df['월']))
print(month)
# plt.pcolor(df)
# plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns)
# plt.yticks(df['월'])
# plt.title('Heatmap by plt.pcolor()', fontsize=20)
# plt.xlabel('Year', fontsize=14)
# plt.ylabel('Month', fontsize=14)
# plt.colorbar()
# plt.show()


# plt.rcParams['figure.figsize'] = [20, 10]
# plt.boxplot(df.loc[:, '피자헛':'피자헤븐'])
# plt.title("TOP10 피자 브랜드 일일 검색량", size = 20)
# plt.show()

# 40 이상인 이상치 값은 제거한다.
df[df['반올림피자샵'] >= 40]  = 0
df[df['피자나라치킨공주'] >= 40]  = 0
print(df.describe())
# search_mean = df.describe()
# search_mean.to_csv("mean.csv", encoding = "cp949")

# plt.rcParams['figure.figsize'] = [20, 10]
# plt.boxplot(df.loc[:, '피자헛':'피자헤븐'])
# plt.title("TOP10 피자 브랜드 일일 검색량(40 이하)", size = 20)
# plt.show()

# plt.rcParams['figure.figsize'] = [20, 10]
# plt.plot(df.loc[:, '피자헛':'피자헤븐'])
# plt.boxplot(df.loc[:, '피자헛':'피자헤븐'])
# plt.title("TOP10 피자 브랜드 일일 검색량(40 이하)", size = 20)
# plt.show()



search_mean = df.mean().sort_values(ascending = False)
print(search_mean)
# label = ['도미노피자', '피자헛', '피자나라치킨공주', '피자마루', '피자알볼로', '미스터피자', '파파존스', '7번가피자', '반올림피자샵', '피자헤븐']
# plt.figure(figsize=(12, 6))  
# plt.bar(label, search_mean, color='slateblue')
# plt.title("TOP10 피자 브랜드 평균 일일 검색량 순위", size = 15)
# plt.show()



