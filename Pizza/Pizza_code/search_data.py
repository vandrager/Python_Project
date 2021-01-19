import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import matplotlib as mat
import seaborn as sns
mat.rcParams['font.family'] = 'Black Han Sans'
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")
brand = ['피자헛', '파파존스', '도미노피자', '반올림피자샵', '미스터피자', '피자마루', '피자알볼로', '피자나라치킨공주', '7번가피자', '피자헤븐']

df = round(pd.read_excel("daily_search.xlsx"), 3)
print(df.head())
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
print(round(search_mean, 2))
# label = ['도미노피자', '피자헛', '피자나라치킨공주', '피자마루', '피자알볼로', '미스터피자', '파파존스', '7번가피자', '반올림피자샵', '피자헤븐']
# plt.figure(figsize=(12, 6))  
# plt.bar(label, search_mean, color='slateblue')
# plt.title("TOP10 피자 브랜드 평균 일일 검색량 순위", size = 15)
# plt.show()


## 월별 히트맵 그리기
# df.set_index('날짜', inplace = True)
month_group = df.groupby(['월'])

# 월별 데이터 평균 훑어보기
for key, group in month_group:
    print("* key :", key)
    print("* number :", len(group))
    print(group.mean())
    print('\n')


# 월별 데이터 평균 구하기
month_mean = df.groupby(df['월']).mean()
print(round(month_mean, 3))

# heatmap 그래프 출력하기(자료형태: 데이터 프레임)
plt.figure(figsize = (20, 8))
sns.heatmap(month_mean, cmap='Blues', annot = True)  # annot = True 히트맵 위에 값 표시
plt.show()

# month_mean.to_excel("month_mean.xlsx")

# treemap 출력하기
df_pivot = df.pivot_table(index = '연', values = ['피자헛', '파파존스', '도미노피자', '반올림피자샵', '미스터피자', '피자마루', '피자알볼로', '피자나라치킨공주', '7번가피자', '피자헤븐'], aggfunc = 'mean')
print(df_pivot)
import squarify
labels = ['7번가피자', '도미노피자', '미스터피자', '반올림피자샵', '파파존스', '피자나라치킨공주', '피자마루', '피자알볼로', '피자헛', '피자헤븐']
colors = ['yellow', 'aqua', 'violet', 'salmon', 'gold', 'olive', 'beige', 'teal', 'darkblue', 'seagreen']
squarify.plot(sizes = df_pivot.loc['2020', '7번가피자':'피자헤븐'], label=labels, color=colors)
plt.show()


## 2020년 피자 브랜드 검색량 최다 조회수 일자 구하기
# df원본 불러오기(이상치값 포함)
df = round(pd.read_excel("daily_search.xlsx"), 3)
df['날짜'] = df['날짜'].astype('str') # 문자열 메소드 사용을 위해 자료형 변경
dates = df['날짜'].str.split('-') # 문자열을 split 메소드로 분리
# print(dates.head())
df['연'] = dates.str.get(0)
df['월'] = dates.str.get(1)
df['일'] = dates.str.get(2)

# print(df.sort_values(ascending = False))
# df.mean().sort_values(ascending = False)
print(df.head())
print(df.loc[:, "피자헛":"피자헤븐"].idxmax())
max_match = df.loc[:, "피자헛":"피자헤븐"].idxmax()
print(max_match.keys())
print(max_match.values)


for index, c in enumerate(max_match.values):
    print("="*50)
    print(f"브랜드명: {brand[index]}")
    print(f"최다조회수 날짜: {df.iloc[c, 0]}")
    print(f"{round(df.iloc[c, index+1], 2)}점")
    print("")