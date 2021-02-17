import os
import re
import pandas as pd
import numpy as np

os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset\1차 분석")

df = pd.read_excel("Review_7.xlsx")

gdf = df.groupby(['브랜드명', '메뉴구분'])

for key, group in gdf:
    print("* key :", key)
    print("* number :", len(group))
    mean = round(group['별점'].mean(), 2)
    count = group['별점'].count()
    print(mean)
    print(format(count, ","))