#test
# https://coinone.co.kr/exchange/trade/eth/krw 에서 이더리움의 시간당 금액을 추출해보자.
# 차트같은 경우에 html에 가격정보가 없다. -> 네트워크탭에 들어가서 가격데이터를 찾자.
import requests
from bs4 import BeautifulSoup
import json

데이터 = requests.get('https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/ETH?lastDt=1703512800000&interval=15m&1704592866093')
# print(데이터.content)
# 데이터가 ""으로 되어 있다 ==> json이다.
# json 데이터를 딕셔너리{''}로 바꿔줘야 편하게 사용할 수 있다.

# # 그러기 위해선 import json을 해줘야함.
딕셔너리 = json.loads(데이터.content) # 이러면 딕셔너리로 됨
# print(딕셔너리)


#Tip!! url을 웹페이지에서 요청하고 json파일로 저장-> 우클릭(Format Document) 하면 이뻐짐

# {{[{}]}} 이렇게 되어 있으니 차례대로 뽑아보자.

print(딕셔너리['body']['candles'][0]['close'])
print(딕셔너리['body']['candles'][1]['close'])
# 이렇게 바꾸면 종가들을 가져올 수 있겠다