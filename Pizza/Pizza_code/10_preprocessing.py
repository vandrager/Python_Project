import pandas as pd
import numpy as np
import os
import datetime
import re


os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset\row_data")

'''
# 서울 & 제외 지역 데이터 통합
file1 = pd.read_excel("seoul_total.xlsx")
file2 = pd.read_excel("not_seoul.xlsx")
df = pd.concat([file1, file2])
df.to_excel("total_review.xlsx")
'''


# 데이터 전처리 작업
df = pd.read_excel("total_review.xlsx")
df.reset_index()
df.drop_duplicates(['브랜드', '일자', '주문메뉴', '리뷰'])

# 지역 전처리
location = df['주소'].str.split(' ') # 문자열을 split 메소드로 분리
df['지역구분'] = location.str.get(0)
df.drop(["주소"], axis=1, inplace=True)

# 브랜드 - 지점명 분리
fran = df['브랜드'].str.split("-")
df['브랜드명'] = fran.str.get(0)
df['지점명'] = fran.str.get(1)
df.drop("브랜드", axis=1, inplace=True)

# 날짜 전처리 ( 형식에 맞지 않는 방금, 며칠 전, 몇 시간 전 등 제거 )
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
df['브랜드명'].replace('미스터피자Single메뉴', "미스터피자", inplace = True)
df['브랜드명'].replace('김준현의 피자헤븐', "김준현의피자헤븐", inplace = True)
for i in range(len(df)):
    try:
        df['메인메뉴'][i] = df['메인메뉴'][i].replace("페퍼로니", "페페로니") # 페퍼로니 페페로니로 통합
    except:
        pass

# 메인 메뉴 괄호와 괄호 안의 텍스트 모두 제거
my_regex = "\(.*\)|\s-\s.*"
for i in range(len(df)):
    try:
        df['메인메뉴'][i] = re.sub(my_regex, '', df['메인메뉴'][i])
        text = df['메인메뉴'][i]
        df['메인메뉴'][i] = " ".join(text.split()).strip()
        df['메인메뉴'][i] = df['메인메뉴'][i].replace("R/1", "")
        df['메인메뉴'][i] = df['메인메뉴'][i].replace("L/1", "")
    except:
        pass

# 데이터 전처리 작업 실행 ( 메뉴 )
df['메뉴구분'] = ""
menu = ['베이컨', '고르곤졸라', '콤비네이션', '스테이크', '쉬림프', '포테이토', '치킨', '고구마', '불고기', '하와이안', '페페로니']
for i in range(len(df)):
    list_a = []
    for k in menu:
        if k in df['메인메뉴'][i]:
           list_a.append(k)
           df['메뉴구분'][i] = " ".join(list_a)
    if pd.isnull(df['메뉴구분'][i]) == True:
        df['메뉴구분'][i] = "기타"


# 데이터 전처리 작업 실행 ( 그룹 )
df['그룹구분'] = "plz success"
set_list = ['SET', '세트', 'set']
for j in range(len(df)):
    try:
        if pd.isnull(df['메뉴2'][j]) == False:
            df['그룹구분'][j] = "Side"
        elif pd.isnull(df['메뉴2'][j]) == True:
            df['그룹구분'][j] = "Single"
        for k in set_list:
            if (k in df['주문메뉴'][j]) | (pd.isnull(df['메뉴3'][j]) == False):
                df['그룹구분'][j] = "Party"
    except:
        pass

# 불필요한 열 제거 /열 순서 수정 후 최종본 저장
df.drop(["Unnamed: 0", "Unnamed: 0.1", "일자", "메뉴2", "메뉴3"], axis=1, inplace=True)
df = df[['지역구분', '브랜드명', '지점명', '주문메뉴', '메인메뉴', "메뉴구분", '그룹구분', '별점', '맛', '양', '배달', '리뷰', '연', '월', '일', 'date', 'weekday']]

os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")
df.to_excel("total_review.xlsx")

