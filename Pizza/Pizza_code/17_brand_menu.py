import pandas as pd
import numpy as np
import os
import datetime
import re
from openpyxl import Workbook


# # 브랜드별 엑셀 데이터 생성
# os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")
# df = pd.read_excel("review_modifi.xlsx")
# brand = ['김준현의피자헤븐', '피자헛', '반올림피자샵','피자알볼로', '피자나라치킨공주','7번가피자', '미스터피자', '파파존스피자', '도미노피자','피자마루']
# os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset\brand")
# for i in range(10):
#     df_set = df[df['브랜드명'] == brand[i]]
#     df_set.to_excel(f"brand_{i}.xlsx",  encoding= "cp949")
#     print(f"브랜드 추출완료 {i+1}번째")



os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset\brand")

df = pd.read_excel("brand_0.xlsx")
df['메인메뉴'] = 0
for i in range(len(df)):
    text = df['주문메뉴'][i].split(",")
    df['메인메뉴'][i] = text[0]
print(df['메인메뉴'].head())

# 판다스 데이터프레임에서 특정한 값의 빈도를 계산
freq = df.groupby(['메인메뉴'])['메인메뉴'].count() 
print(freq)