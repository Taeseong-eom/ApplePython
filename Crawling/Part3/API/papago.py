# 파파고 API를 활용한 번역봇을 만들어보자.

import os
import sys
import urllib.request
import json

def 번역기(data):
    client_id = "6kuRNmIph15ctCipCvg6" # 개발자센터에서 발급받은 Client ID 값
    client_secret = "5ZBm85vFEx" # 개발자센터에서 발급받은 Client Secret 값
    encText = urllib.parse.quote(data)
    data = "source=en&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        딕셔너리 = json.loads(response_body)
        return 딕셔너리['message']['result']['translatedText']
    else:
        print("Error Code:" + rescode)


번역기('hello')

# 이제 이걸 모듈화하서 엑셀파일 한번에 번역해보자.
    

