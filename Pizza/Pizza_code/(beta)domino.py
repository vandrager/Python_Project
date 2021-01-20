import os, re
import requests
from bs4 import BeautifulSoup as bs
import urllib.request as ur
from openpyxl import workbook

os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Project_python\Pizza\Dataset")
url = "https://web.dominos.co.kr/goods/list?dsp_ctgr=C0101"
res = requests.get(url)
res.raise_for_status()
soup = bs(ur.urlopen(url).read(), 'html.parser')

title = "피자명,라지가격,미디움가격,설명,이미지".split(",")
menu_list = soup.find_all("div", attrs={"class": "menu-list"})

for menu in menu_list:
    for i in menu:
        name = i.text
        print(name)
    
# for d in do_list:
#     menu = d.get_text().strip()
    

# do_list = soup.find_all('span', attrs={"class": "size_l"})
# for d in do_list:
#     menu = d.get_text().strip()
    

# do_list = soup.find_all('div', attrs={"class": "subject"})
# for d in do_list:
#     menu = d.get_text().strip()
    

# do_list = soup.find_all('div', attrs={"class": "subject"})
# for d in do_list:
#     menu = d.get_text().strip()
    



# f.close()


# f.see
# for page in range(1, 5):
#     res = requests.get(url + str(page))
#     res.raise_for_status()
#     soup = BeautifulSoup(res.text, "lxml")
#     data_rows = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")

#     for row in data_rows:
#         columns = row.find_all("td")
#         if len(columns) <= 1: #의미없는 데이터는 skip
#             continue
#         data = [column.get_text().strip() for column in columns]
#         print(menu)
#         writer.writerow(data)

#     print(data[0])