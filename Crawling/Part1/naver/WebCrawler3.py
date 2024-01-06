import requests
from bs4 import BeautifulSoup


def 현재가(기업코드):
    데이터 = requests.get(f'https://finance.naver.com/item/sise.nhn?code={기업코드}') # 변수를 넣으려면 {} 안에 넣고 앞에 f(포맷팅)를 붙여야한다.
    soup = BeautifulSoup(데이터.content, 'html.parser')
    print(soup.find_all('strong', id="_nowVal")[0].text)
    return soup.find_all('strong', id="_nowVal")[0].text

print("삼성전자 현재가")
현재가('005930')

f = open('WebCrawler3.csv', 'w')
f.write(현재가('005930'))
f.close()