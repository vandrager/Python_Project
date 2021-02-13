import os
import re
import pandas as pd
import numpy as np
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset\hoho")

'''
# 전처리 마무리
df = pd.read_excel("menu_final.xlsx", header = 0)
df['브랜드명'].replace("미스터피자Single메뉴", "미스터피자", inplace = True)
df['브랜드명'].replace("피자헤븐", "김준현의피자헤븐", inplace = True)
df.drop_duplicates(subset=['브랜드명', '가격', '메뉴명'], inplace = True)
df = df[['브랜드명', '메뉴명', '가격', '이미지']]
print(df.head(5))
df.to_excel("menu_final.xlsx")
'''

df = pd.read_excel("menu_final.xlsx", header = 0)
df.columns = ['index', '브랜드명', '메뉴명', '가격', '이미지']
print(df.columns)
print(df.head(4))