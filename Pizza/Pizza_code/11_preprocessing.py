import pandas as pd
import numpy as np
import os
import datetime


os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")

df = pd.read_excel("seoul_19.xlsx")
print(len(df))
# df.reset_index()
# df.drop_duplicates(['브랜드', '일자', '주문메뉴', '리뷰'])
# df.drop(['Unnamed: 0', "Unnamed: 0.1"], axis=1, inplace=True)

# 지역 전처리
location = df['자치구'].str.split(' ') # 문자열을 split 메소드로 분리

df['시'] = location.str.get(0)
df['구'] = location.str.get(1)
df['동'] = location.str.get(2)
df['도로명'] = location.str.get(3)
df.drop(["자치구", "동", "도로명"], axis=1, inplace=True)

# 브랜드 - 지점명 분리
fran = df['브랜드'].str.split("-")

df['브랜드명'] = fran.str.get(0)
df['지점명'] = fran.str.get(1)
df.drop("브랜드", axis=1, inplace=True)

# 날짜 전처리
# 형식에 맞지 않는 방금, 며칠 전, 몇 시간 전 등 제거부터
for i in range(len(df)):
    if df['일자'][i][-1] != "일":
        df['일자'][i] = np.nan
df.dropna(axis = 0, inplace= True)

time = df['일자'].str.split(" ")
df['연'] = time.str.get(0)
df['월'] = time.str.get(1)
df['일'] = time.str.get(2)
df['date'] = df['연'] + df['월'] + df['일']

# 1. 요일 컬럼 만들고 2020-12-25 날짜 형식으로 만들어주자
df.drop("일자", axis=1, inplace=True)

# 열 순서 바꿔주고 저장하기
df.columns = ["딘딘 네모의꿈"]
df.to_excel("erra.xlsx")
