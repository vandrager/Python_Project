import pandas as pd
import os
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset\소상공인시장진흥공단_상가(상권)정보_20200930")
# df1 = pd.read_csv("소상공인시장진흥공단_상가(상권)정보_강원_202009.csv", encoding="cp949")
# df2 = pd.read_csv("소상공인시장진흥공단_상가(상권)정보_경기_202009.csv", encoding="cp949")
# df3 = pd.read_csv("소상공인시장진흥공단_상가(상권)정보_경남_202009.csv", encoding="cp949")
# df4 = pd.read_csv("소상공인시장진흥공단_상가(상권)정보_경북_202009.csv", encoding="cp949")
# df5 = pd.read_csv("소상공인시장진흥공단_상가(상권)정보_광주_202009.csv", encoding="cp949")
# df6 = pd.read_csv("소상공인시장진흥공단_상가(상권)정보_대구_202009.csv", encoding="cp949")
# df7 = pd.read_csv("소상공인시장진흥공단_상가(상권)정보_대전_202009.csv", encoding="cp949")
# df8 = pd.read_csv("소상공인시장진흥공단_상가(상권)정보_부산_202009.csv", encoding="cp949")
# df9 = pd.read_csv("소상공인시장진흥공단_상가(상권)정보_서울_202009.csv", encoding="cp949")
# df10 = pd.read_csv("소상공인시장진흥공단_상가(상권)정보_세종_202009.csv", encoding="cp949")
# df11 = pd.read_csv("소상공인시장진흥공단_상가(상권)정보_울산_202009.csv", encoding="cp949")
# df12 = pd.read_csv("소상공인시장진흥공단_상가(상권)정보_인천_202009.csv", encoding="cp949")
# df13 = pd.read_csv("소상공인시장진흥공단_상가(상권)정보_전남_202009.csv", encoding="cp949")
# df14 = pd.read_csv("소상공인시장진흥공단_상가(상권)정보_전북_202009.csv", encoding="cp949")
# df15 = pd.read_csv("소상공인시장진흥공단_상가(상권)정보_제주_202009.csv", encoding="cp949")
# df16 = pd.read_csv("소상공인시장진흥공단_상가(상권)정보_충남_202009.csv", encoding="cp949")
# df17 = pd.read_csv("소상공인시장진흥공단_상가(상권)정보_충북_202009.csv", encoding="cp949")

# full_df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17])
# print(full_df.info())

df1 = pd.DataFrame([[1, 2, 3],
                    [2, 3, 4]],
                    columns = ["원", "투", "쓰리"])
df2 = pd.DataFrame([[3, 6, 8],
                    [1, 6, 4]],
                    columns = ["원", "투", "쓰리"])
result = [df1, df2]
count = 0
for i in result:
    count += len(i["원"])
    print(i["원"])
print(count)
# result.to_csv("full.csv", encoding = "cp949")
# full_df.to_csv("full_data.csv", encoding = "cp949")