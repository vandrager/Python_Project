import numpy as np
import pandas as pd
import os
import re
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")

df = pd.read_csv("rko.csv", encoding = 'cp949')
my_regex = "\(.*\)|\s-\s.*"
for i in range(len(df)):
    try:
        df['내용'][i] = re.sub(my_regex, '', df['내용'][i])
        text = df['내용'][i]
        df['내용'][i] = " ".join(text.split()).strip()
        df['내용'][i] = df['내용'][i].replace("L/1", "")
        df['내용'][i] = df['내용'][i].replace("R/1", "")
    except:
        pass
print(df.head())
print(len(df))
df.to_csv("doublerko.csv")