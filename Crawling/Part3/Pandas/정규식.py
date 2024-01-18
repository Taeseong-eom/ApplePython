# 정규식 : 문자를 검사하는 식
# 정규식으로 데이터 전처리를 하자.
import re

# print(re.search('정규식', '안녕하세요정규식')) # 있으면 object 자료를 출력하고 없으면 None을 뱉음
a = re.findall('a', 'abcdefg') # a가 있나?
a = re.findall('^a', 'abcdefg') # a로 시작하나?
a = re.findall('g$', 'abcdefg') # g로 끝나나?
a = re.findall('\$', 'abcde$f^g') # 특수기호 찾기

a = re.findall('[ab]', 'abcde$f^g') # a 또는 b가 있는지
a = re.findall('[a-z]', 'abcde$f^g') # a 부터 z 까지 있는지
a = re.findall('[a-zA-Z]', 'abcde$f^g') # a 부터 z 까지 또는 A 부터 Z 까지 있는지
a = re.findall('[가-힣ㄱ-ㅎ]', 'abcdeㄴㅋㅋㅋㅋ$f^gㄱ안녕하세요') # 가 부터 힣 까지 또는 ㄱ 부터 ㅎ까지 있는지
a = re.findall('[0-9]', 'abcd1234eㄴㅋㅋㅋㅋ$f^gㄱ안녕하세요') # 숫자가 있는지
a = re.findall('[^0-9]', 'abcd1234eㄴㅋㅋㅋㅋ$f^gㄱ안녕하세요') # 숫자가 아닌것이 있는지 ^(not)
a = re.findall('\d', 'abcd12334eㄴㅋㅋㅋㅋ$f^gㄱ안녕하세요') # 숫자가 있는지
a = re.findall('\d\d', 'abcd12334eㄴㅋㅋㅋㅋ$f^gㄱ안녕하세요') # 숫자 뒤에 숫자가 있는게 있는지
a = re.findall('\d{3}', 'abcd12334eㄴㅋㅋㅋㅋ$f^gㄱ안녕하세요') # 세자리 숫자가 있는지
a = re.findall('\D', 'abcd12334eㄴㅋㅋㅋㅋ$f^gㄱ안녕하세요') # 숫자가 아닌것이 있는지
a = re.findall('\s', 'abcd12334  eㄴㅋㅋㅋㅋ$  f^gㄱ안녕하세요') # 스페이스바가 있는지
a = re.findall('\S', 'abcd12334  eㄴㅋㅋㅋㅋ$  f^gㄱ안녕하세요') # 스페이스바가 아닌 문자가 있는지

a = re.findall('ㅋ+', 'abcd12334  eㄴㅋㅋㅋㅋ$  f^gㄱ안녕하세요') # 반복되는 문자 찾을때
a = re.findall('abc', 'abcd12334  eㄴㅋㅋㅋㅋ$  f^gㄱ안녕하세요',re.IGNORECASE) # 대소문자 가리지 않고 찾아줌 

# print(a) # 있으면 리스트로 이쁘게 출력함.

print(re.sub('\-','','2022-1-1') ) # 2022-1-1 에서 -를 .으로 바꿔
print(re.sub('\D','','2abcd12334  eㄴㅋㅋㅋㅋ$  f^gㄱ안녕하세요') ) # 숫자 제거

# 나머지는 검색해서 찾아서 쓰자.


결과 = re.findall('@[a-z+]+\.+[a-z+]', 'abc@example.com',re.IGNORECASE)
print(결과)

