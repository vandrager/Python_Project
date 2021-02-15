import os
import re
import pandas as pd
import numpy as np

os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset\1차 분석")

'''
# 전처리 마무리
file = pd.read_excel("menu_final.xlsx", header = 0)
new = pd.read_excel("menubook_heaven.xlsx", header = 0)
file = pd.concat([file, new])
file.to_excel("menu_final.xlsx")
# df = pd.read_excel("menu_final.xlsx", header = 0)
# df.columns = ['index','브랜드명', '메뉴명', '가격', '이미지']
# print(df.columns)
# print(df.head(4))
'''


df = pd.read_excel("Review_2.xlsx")
book = pd.read_excel("MENU.xlsx")
# menu = df['주문메뉴'].str.split(",")
# df['메인메뉴'] = menu.str.get(0)

'''
# TEST(1) 피자 주문 개수로 그룹구분 만들어보기
print(len(df[df['메인메뉴'].str.contains('/1')])) 254597
print(len(df[df['메인메뉴'].str.contains('/2')])) 666
print(len(df[df['메인메뉴'].str.contains('/3')])) 97
-> 피자는 대부분 한 판만 주문해서 먹는다 그룹구분이 무의미함

# TEST(2) 특정 키워드로 그룹구분 만들어보기
print(len(df[df['메인메뉴'].str.contains('SET')])) 1188
print(len(df[df['메인메뉴'].str.contains('세트')])) 75121
print(len(df[df['메인메뉴'].str.contains('하프')])) 10697
-> 생각보다 하프앤하프 사이즈가 적게 나옴

# TEST(3) 피자 사이즈로 그룹구분 만들어보기
print(len(df[df['메인메뉴'].str.contains('R')])) 60422
print(len(df[df['메인메뉴'].str.contains('MONSTER')])) # REPLACE 필요 915
print(len(df[df['메인메뉴'].str.contains('L')])) 158499
print(len(df[df['메인메뉴'].str.contains('M')])) 31029
print(len(df[df['메인메뉴'].str.contains('F')])) 2106
print(len(df[df['메인메뉴'].str.contains('P')])) 728
# F or p 등 기타 사이즈는 BIG으로 구분
'''

'''
df['그룹구분'] = 0
for i in range(len(df)):
    if "R" in df['메인메뉴'][i]:
        df['그룹구분'][i] = "Regular"
    elif "M" in df['메인메뉴'][i]:
        df['그룹구분'][i] = "Medium"
    elif "L" in df['메인메뉴'][i]:
        df['그룹구분'][i] = "Large"
    elif "F" in df['메인메뉴'][i]: # 파파존스
        df['그룹구분'][i] = "Big"
    elif "P" in df['메인메뉴'][i]: # 파파존스
        df['그룹구분'][i] = "Big"
    elif "G" in df['메인메뉴'][i]: # 7번가 피자
        df['그룹구분'][i] = "Big"
    elif "BL" in df['메인메뉴'][i]: # 피자헤븐
        df['그룹구분'][i] = "Big"
    elif "BIG L" in df['메인메뉴'][i]: # 피자헤븐
        df['그룹구분'][i] = "Big"
    elif "MONSTER" in df['메인메뉴'][i]: # 반올림
        df['그룹구분'][i] = "Big"
    elif "세트" in df['메인메뉴'][i]: # 피자헤븐
        df['그룹구분'][i] = "Set"
    elif "SET" in df['메인메뉴'][i]: # 피자헤븐
        df['그룹구분'][i] = "Set"
    else:
        df['그룹구분'][i] = "Original"
'''
df['메뉴구분'] = "미분류"
# Pandas dataframe 에서 특정 조건을 충족하면 열 값을 조건으로 바꾸기 
for i in range(len(book)):
    for j in range(len(df)):
        if book['메뉴명'][i] in df['메인메뉴'][j]:
            df['메뉴구분'][j] = book['메뉴명'][i]
        else:
            pass
# df.loc[(df['가격'] > 50) & (df['메인메뉴'] > 30),'리뷰']='test'

'''
* 21/02/25 수정사항 
메뉴북에서 음료/사이드 메뉴는 제거하고 피자만 남겨둔 채로 다시 메뉴구분 만들 것
기타가 약 30% 비율을 차지하고 있음
브랜드별 메뉴 수정(빈칸/누락메뉴 추가)
텍스트 공백제거 코드북도 동일 적용할 것
'''

df.drop("메인메뉴", axis=1, inplace=True)
df = df[['지역구분', '브랜드명', '지점명', '주문메뉴', '메뉴구분', '그룹구분','별점', '맛', '양', '배달', '리뷰', '연', '월', '일', 'date', 'weekday']]
df.to_excel("Review.xlsx")



