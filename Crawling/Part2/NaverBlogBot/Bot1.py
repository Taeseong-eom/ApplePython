from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
import os

# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager #드라이버 대신에 사용(자동 업데이트)
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options


import urllib.request
옵션 = webdriver.ChromeOptions() # 옵션 추가하겠음
#계정정보 넣는 걸 복붙하자.
옵션.add_argument(r'user-data-dir=C:\Users\taeseong\AppData\Local\Google\Chrome\User Data\Default') #\하려면 앞에 r써야함.row data

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=옵션)
driver.get('https://nid.naver.com/nidlogin.login?svctype=262144') # 모바일이 더 쉬워서 모바일로 하겠음.

#캡차를 뚫어야함
# 1. 복사붙여넣기 쓰기 2. 실제 브라우저처럼 꾸미기
time.sleep(2)
pyperclip.copy('djaxotjd95') # 복사
e = driver.find_element(By.CSS_SELECTOR, '#id')
e.send_keys(Keys.CONTROL, 'v') # 이렇게 입력하면 너무 빨리 입력하게 되어 봇을 감지한다. pip install pyperclip(복붙 가능)
# 이렇게 컨트롤 + V 해서 붙여넣기

time.sleep(1)

pyperclip.copy('???') # 복사
e = driver.find_element(By.CSS_SELECTOR, '#pw')
e.send_keys(Keys.CONTROL, 'v') 

time.sleep(1)

e.send_keys(Keys.ENTER)

# 다 추적당하기때문에 인간처럼 동작하게 만들어야함.
time.sleep(1)
driver.get('https://m.naver.com/') 
time.sleep(1)
driver.get('https://m.blog.naver.com/FeedList.naver') 
time.sleep(1)
driver.get('https://blog.editor.naver.com/editor?deviceType=mobile&returnUrl=https%3A%2F%2Fm.blog.naver.com%2FGoWriteForm.naver') 
time.sleep(1)

e = driver.find_element(By.CSS_SELECTOR, '#se_component_wrapper > div:nth-child(1) > div > div.se_sectionArea.se_align-left > div > div > div > div > textarea')
e.send_keys("네이버 자동 블로그 생성")
time.sleep(1)
e = driver.find_element(By.CSS_SELECTOR, '.se_editable')
e.send_keys("테스트입니다.")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '#publishSettingPublic_3').click()
time.sleep(1)

#사진 업로드 추가
driver.find_element(By.CSS_SELECTOR, '#editor_frame > div > div.editor-container > div.header-container > div:nth-child(2) > div > div:nth-child(1) > div.toolbar-wrap.is-scroll > ul > li:nth-child(1) > button').click()
time.sleep(1)
os.system(os.getcwd() + "/FileUpload.exe")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '.btn_applyPost').click()





time.sleep(1000000) #코드 맨 마지막에 추가/ 자동 종료 방지