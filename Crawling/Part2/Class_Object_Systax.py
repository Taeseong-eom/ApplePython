# nunu = {
#     'q':'eat',
#     'w':'snowball' 
# }
# garen = {
#     'q':'strike',
#     'w':'courage'
# }
# 이렇게 하면 자료가 많아지면 힘들다.

# 그럼 어떻게 하면 편하게 할 수 있을까?
# Object를 사용하자.

#유사한 Object를 한줄로 만들수 있다.
class Hero:
    def __init__(self, 구멍):
        self.q = 구멍
        self.w = 'snowball'
    def Hello(self): # 무조건 self를 써야함. self는 새로 생성되는애을 의미함 그래야 자동으로 생성됨
        print("Hello")


nunu = Hero('eat')
garen = Hero('strike')

print(nunu.q)
print(garen.q)
nunu.Hello()
garen.Hello()