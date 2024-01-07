import requests
from bs4 import BeautifulSoup
import json
import time


데이터 = requests.get('https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/ETH?lastDt=1703512800000&interval=15m&1704592866093')
딕셔너리 = json.loads(데이터.content)


# dt는 시간인데 epoch/UNIX 시간이다. 10자리로 구성되어있고 뒤에 추가로 000은 ms를 표현하고 싶을때 사용한다
# 그럼 시간을 우리가 아는 시간으로 어떻게 변환할까?
# import time
# time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(딕셔너리['body']['candles'][i]['dt']/1000)) 


for i in range(200):
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(딕셔너리['body']['candles'][i]['dt']/1000))  + " : ")
    print(str(딕셔너리['body']['candles'][i]['close']) + "\n")


# 이걸로 학습 시키면 코인 가격 예측될듯?s