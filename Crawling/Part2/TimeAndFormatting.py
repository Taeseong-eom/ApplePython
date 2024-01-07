import time

#현재 시간 출력방법
print(time.time())

#처리시간도 잴 수 있음.

#보기 쉽게 출력하기
시간 = time.time()
시간 = time.ctime(시간)
print(시간)

#전부가 아니라 일부만 보고 싶으면??
시간 = time.localtime()
print("현재시간은 " + str(시간.tm_hour) + "시 입니다.")

# strtime()으로 시간표시형식 맘대로 바꾸기
# time.strftime('포맷팅문법', 로컬타임) # 시간을 이쁘게 만드는걸 도와줌
a= time.strftime('%Y year %m month', 시간) # 근데 얘는 한글 잘 못알아들음 그래서 영어로 작성
print(a)

#포맷팅 문법이 뭔가?
#문자 중간에 변수/문자를 넣고 싶을때
name = "Kim"
print('안녕하세요. %s' %name) # 이렇게 할 수 있다.
print(f'안녕하세요 {name}') # 이게 더 최신 문법. 이렇게도 할 수 있다.

#시간더 간단하게 출력해보자
import datetime
a = datetime.datetime(2022, 10 , 1)
print(a)
a = datetime.datetime.now()
print(a)
