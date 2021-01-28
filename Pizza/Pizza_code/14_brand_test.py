import re
import pandas as pd

# 정규식을 이용하여 괄호와 괄호 안 문자열 제거
regex = "\(.*\)|\s-\s.*"
text = "오늘은 딸기(서향딸기, 600g, 1팩 당 5,000원)가 좋습니다!"

print(re.sub(regex, '', text))  # 오늘은 딸기가 좋습니다!
# 가상의 데이터 프레임 생성
df = pd.DataFrame([["asdf(q3de(18)), ( england 2020 )", 2, 3],
                    ["aecf(bwe(34))/ ( korea( 2020 ))", 2, 3],
                    ["nwvf(bsde(6g)) - (china(2020)", 2, 3]],
                    columns = ["브랜드", "키", "몸무게"])
print(df)
'''
가상의 데이터 프레임 구조 확인
                                브랜드  키  몸무게
0  asdf(q3de(18)), ( england 2020 )  2    3
1   aecf(bwe(34))/ ( korea( 2020 ))  2    3
2     nwvf(bsde(6g)) - (china(2020)  2    3
'''
# 브랜드 열 데이터 괄호와 괄호 안 문자열 제거
for i in range(len(df)):
    df['브랜드'][i] = re.sub(regex, '', df['브랜드'][i])
    print(df['브랜드'][i])
'''
정상적으로 괄호와 문자열 제거되는지 확인
asdf
aecf
nwvf
'''

# 최종적으로 수정된 가상의 데이터 프레임 구조 확인
print(df)
'''
    브랜드  키  몸무게
0  asdf  2    3
1  aecf  2    3
2  nwvf  2    3
'''

# 파이썬 문자열 중간 공백 제거하는 방법
text = "오늘은      딸기(서향딸기, 600g, 1팩 당 (5,000원))가      좋습니다!" # 문자열 간 공백의 길이를 다르게 하고 tab을 섞은 문장 생성
text = re.sub(regex, '', text) # 정규식을 통해 괄호와 괄호안 문자열 제거
out = " ".join(text.split())
print(out) # 오늘은 딸기가 좋습니다!

df['브랜드'][0] = "ffff R/1 ok google"
df['브랜드'][1] = "ffff L/1 ok google"
for i in range(len(df)):
    try:
        df['브랜드'][i] = df['브랜드'][i].replace("f", "")
        df['브랜드'][i] = df['브랜드'][i].replace("R/1", "")
        df['브랜드'][i] = df['브랜드'][i].replace("L/1", "")
    except:
        pass
print(df)
'''
           브랜드  브랜드  몸무게
0    ok google  2    3
1    ok google  2    3
2          nwv  2    3
'''
list_ok = []
list_google = []
for i in range(len(df)):
    if "ok" in df['브랜드'][i]:
        df['브랜드'][i] = df['브랜드'][i].replace("google", "")
        list_ok.append(df['브랜드'][i].strip())
    if "ok" in df['브랜드'][i]:
        df['브랜드'][i] = df['브랜드'][i].replace("ok", "google")
        list_google.append(df['브랜드'][i].strip())


print(list_ok)
print(list_google)

df = pd.DataFrame([["asdf(q3de(18)), ( england 2020 )", 2, 3],
                    ["aecf(bwe(34))/ ( korea( 2020 ))", 2, 3],
                    ["nwvf(bsde(6g)) - (china(2020)", 2, 3]],
                    columns = ["브랜드", "주문메뉴", "주문취향"])

# 워드클라우드를 통해 주문 메뉴 리스트 추출
# 브랜드별로 페페로니 페퍼로니 메뉴명이 다름 페페로니로 전처리 필요함
menu = ['베이컨', '고르곤졸라', '치즈', '콤비네이션', '스테이크', '쉬림프', '포테이토', '치킨', '고구마', '불고기', '하와이안', '페페로니']
group = ['Single', 'Set', 'Side', 'Party']
brand = ['피자헛', '파파존스', '도미노피자', '반올림피자샵', '미스터피자', '피자마루', '피자알볼로', '피자나라치킨공주', '7번가피자', '피자헤븐']
