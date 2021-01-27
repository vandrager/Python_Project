import pandas as pd
import numpy as np
import os
import datetime
import re


os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset\row_data")

# 전체 데이터
df = pd.read_excel("seoul_total.xlsx")
# 샘플 데이터
# df = pd.read_excel("seoul_total.xlsx")
df.reset_index()
df.drop_duplicates(['브랜드', '일자', '주문메뉴', '리뷰'])
df.drop(['Unnamed: 0', "Unnamed: 0.1"], axis=1, inplace=True)

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

# 문자열을 슬라이싱해서 자르기 (년, 월, 일 제거)
df["연"] = df['연'].str.slice(start=0, stop=-1)
df["월"] = df['월'].str.slice(start=0, stop=-1)
df["일"] = df['일'].str.slice(start=0, stop=-1)
df['date'] = df['연'] + "-" + df['월'] + "-" + df['일']
df['date'] = pd.to_datetime(df['date'])
df['weekday'] = df['date'].dt.strftime("%A")

# 주문메뉴 전처리
menu = df['주문메뉴'].str.split(",")
df['메인메뉴'] = menu.str.get(0)
df['메뉴2'] = menu.str.get(1)
df['메뉴3'] = menu.str.get(2)
df['메뉴4'] = menu.str.get(3)
df['단품주문'] = df['메뉴2'].isnull()
df['다량주문'] = df['메뉴4'].notnull()
df['브랜드명'].replace('미스터피자Single메뉴', "미스터피자", inplace = True)
df['브랜드명'].replace('김준현의 피자헤븐', "김준현의피자헤븐", inplace = True)

# 메인 메뉴 괄호와 괄호 안의 텍스트 모두 제거
my_regex = "\(.*\)|\s-\s.*"
for i in range(len(df)):
    try:
        df['메인메뉴'][i] = re.sub(my_regex, '', df['메인메뉴'][i])
    except:
        pass


# 열 순서 바꿔주고 저장하기
df.drop(["일자", "메뉴2", "메뉴3", "메뉴4"], axis=1, inplace=True)
df = df[['시', '구', '브랜드명', '지점명', '주문메뉴', '메인메뉴', '별점', '맛', '양', '배달', '리뷰', '연', '월', '일', 'date', 'weekday', '단품주문', '다량주문']]

os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")
df.to_excel("seoul_review.xlsx")

print(df.head())
print(df.info())