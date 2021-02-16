import os
import re
import pandas as pd
import numpy as np

os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset\1차 분석")

df = pd.read_excel("Review_5.xlsx")

'''
# 사이드 메뉴 전처리
df['메뉴구분'].replace("콜라", "기타", inplace = True)
df['메뉴구분'].replace("콜라1.25L", "기타", inplace = True)
df['메뉴구분'].replace("콜라500ml", "기타", inplace = True)
df['메뉴구분'].replace("스프라이트1.5L", "기타", inplace = True) 
df['메뉴구분'].replace("코카콜라1.25L", "기타", inplace = True)
df['메뉴구분'].replace("코카-콜라1.25L", "기타", inplace = True)
df['메뉴구분'].replace("갈릭소스", "기타", inplace = True)
df['메뉴구분'].replace("핫소스", "기타", inplace = True)
df['메뉴구분'].replace("디핑소스", "기타", inplace = True)
df['메뉴구분'].replace("치즈스틱", "기타", inplace = True)
df['메뉴구분'].replace("치즈오븐스파게티", "기타", inplace = True)
-----반올림피자샵------
세트1（피자L＋스파게티＋콜라500ml）
세트2（피자L＋스파게티＋핫윙＋콜라1.25L）
세트5（피자R＋스파게티＋콜라500ml）
세트6（피자R＋스파게티＋핫윙＋콜라1.25L)
-----피자헛------


df.to_excel("Review_4.xlsx")
'''


gdf = df.groupby(['브랜드명', '메뉴구분'])['별점'].count()
gdf.to_excel("ff.xlsx")