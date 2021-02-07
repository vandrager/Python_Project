# review data timegraph analysis
'''
메뉴구분별 월 주문건수 추이 분석(M)
브랜드별 주문건수 추이 분석(Date)
평일/주말 그룹구분 or 브랜드별 주문건수 추이 분석(weekday)
연도별 브랜드 주문건수 추이 분석(Y)
요일별 별점/메뉴 구분 분석
'''

import pandas as pd
import numpy as np
import os
from bs4 import BeautifulSoup as bs
import urllib.request as ur
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from openpyxl import Workbook #  결과물을 엑셀 파일로 저장

os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")
df = pd.read_excel("sample.xlsx")