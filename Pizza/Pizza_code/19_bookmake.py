import os
import requests as re
import pandas as pd
import numpy as np
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset\hoho")

# 브랜드별 메뉴 통합
# file = pd.read_excel("menubook_0.xlsx")
# for i in range(1, 13):
#     new = pd.read_excel("menubook_{}.xlsx".format(i))
#     file = pd.concat([file, new])
# file.to_excel("menu_total.xlsx")

df = pd.read_excel("menu_total.xlsx")
fran = df['브랜드'].str.split("-")
df['브랜드명'] = fran.str.get(0)

df["가격"] = df['가격'].str.slice(start=0, stop=-1)
df['가격'] = df['가격'].apply(lambda x: x.replace(',', ''))
print(df['가격'].head())
print(df.info())
df['가격'] = pd.to_numeric(df['가격'])
df.drop(['브랜드', 'Unnamed: 0'], axis = 1, inplace = True)
df.drop_duplicates(subset=['브랜드명', '가격', '메뉴명'], inplace = True) # 중복 메뉴 제거
for i in range(len(df)):
    try:
        if df['이미지'][i] == "background-image: url(''), url('image/ic_photomenu_default.png');":
            df['이미지'][i] = 0
        else:
            df['이미지'][i] = df['이미지'][i].str.slice(start=0, stop=-1)
    except:
        pass
print(df.columns)
df = df[['브랜드명', '가격', '메뉴명', '이미지']]
print(df.info())
print(df.head())
df.to_excel("menu_final.xlsx")