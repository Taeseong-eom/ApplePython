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

# # map 사용법
# # 리스트[1,2,3,4,5] 에 각각 1을 더하고 싶으면? 
# # map(함수,리스트) 쓰면 함수를 리스트에 각각 적용시킬 수 있음
# 리스트 = [1,2,3,4,5] 
# def 더한다(x):
#     return x + 1
# result = map(더한다,리스트)
# print(list(result))


def 이더리움가격불러온다(유알엘):
    data = requests.get(유알엘)
    딕셔너리 = json.loads(data.content)
    #print(딕셔너리['data'][0]['Close'])
    return 딕셔너리['data'][0]['Close']

# 이더리움가격불러온다(url[0])

from multiprocessing.dummy import Pool as ThreadPool # 멀티프로세싱 라이브러리를 쓰겠다 
# 뒤에 .dummy를 붙이면 멀티쓰레딩을 하겠다는 거임

pool = ThreadPool(4) # Thread를 4개 띄우겠다

result = pool.map(이더리움가격불러온다,url) # url을 하나씩 이더리움가격불러온다에 넣는다. 결과를 result에 넣는다

pool.close() # 작업종료하자
pool.join() # 결과나올때까지 기다려

print(result)

# 수집한 url을 url 리스트에 다 저장하고 꺼내서 사용하면 되겠다.
