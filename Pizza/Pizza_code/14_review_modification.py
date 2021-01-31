import os
import pandas as pd

os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")
df = pd.read_excel("total_review.xlsx")

menu = df['주문메뉴'].str.split(",")
df['메인메뉴'] = menu.str.get(0)
df['메뉴2'] = menu.str.get(1)
df['메뉴3'] = menu.str.get(2)

# 데이터 전처리 작업 실행 ( 메뉴 )
menu = ['베이컨', '고르곤졸라', '치즈', '콤비네이션', '스테이크', '쉬림프', '포테이토', '치킨', '고구마', '불고기', '하와이안', '페페로니']
for i in range(len(df)):
    try:
        for k in menu:
            if k in df['메인메뉴'][i]:
                df['메뉴구분'][i] += k
        if df['메뉴구분'][i] == "":
            df['메뉴구분'][i] = "기타"
    except:
        pass

# 데이터 전처리 작업 실행 ( 그룹 )
set_list = ['SET', '세트', 'set']
for j in range(len(df)):
    try:
        if pd.isnull(df['메뉴2'][j]) == False:
            df['그룹구분'][j] = "Side"
        elif pd.isnull(df['메뉴2'][j]) == True:
            df['그룹구분'][j] = "Single"
        for k in set_list:
            if (k in df['주문메뉴'][j]) | pd.isnull(df['메뉴3'][j]) == False:
                df['그룹구분'][j] = "Party"
    except:
        pass

# 열 순서 바꿔주고 저장하기
df.drop(["메뉴2", "메뉴3"], axis=1, inplace=True)

df.to_excel("total_review(modi).xlsx")