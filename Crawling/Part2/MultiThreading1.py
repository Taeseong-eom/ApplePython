import requests
import time
import json

url = [
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1609524000000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608811200000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608098400000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1606672800000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605960000000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605242700000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1604534400000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603821600000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603108800000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1602396000000',
]

data = requests.get(url[0])
딕셔너리 = json.loads(data.content)
print(딕셔너리['data'][0]['Close'])

data = requests.get(url[1])
딕셔너리 = json.loads(data.content)
print(딕셔너리['data'][0]['Close'])

# 이걸 for 써서 반목하면 순서대로 하느라 오래걸림
# 그래서 멀티프로세싱이나 멀티스레딩을 통해 동시에 실행하자

def 이더리움가격불러온다(유알엘):
    data = requests.get(유알엘)
    딕셔너리 = json.loads(data.content)
    print(딕셔너리['data'][0]['Close'])

이더리움가격불러온다(url[0])

# 멀티스레드 해도 원하는대로 안될 수 있음. 하나의 데이터를 쓰는 경우 병목이 발생

from multiprocessing.dummy import Pool as ThreadPool # 멀티프로세싱 라이브러리를 쓰겠다 
# 뒤에 .dummy를 붙이면 멀티쓰레딩을 하겠다는 거임

pool = ThreadPool(4) # Thread를 4개 띄우겠다
pool.map() # 뭐를 멀티프로세싱 작업할지

pool.Close() # 작업종료하자
pool.join() # 결과나올때까지 기다려



