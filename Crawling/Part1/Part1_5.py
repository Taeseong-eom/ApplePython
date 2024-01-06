import requests
from bs4 import BeautifulSoup

def 현재가(기업코드):
    데이터 = requests.get(f'https://finance.naver.com/item/sise.nhn?code={기업코드}')
    soup = BeautifulSoup(데이터.content, 'html.parser')
    print(soup.find_all('strong', id="_nowVal")[0].text)
    return soup.find_all('strong', id="_nowVal")[0].text

종목들 = ['005930','066575','005380','035720','034220','003490']

# 종목들의 기업코드를 통해 현재가 함수로 기업들의 현재가를 txt 파일로 저장

파일 = open('Part1_5.txt', 'w')
for i in 종목들:
    파일.write(현재가(i) + '\n')
파일.close()
