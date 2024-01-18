# 엑셀 대신 panda 쓰면 더 빠르게 통계 낼 수 있음.
import pandas as pd 
#데이터 프레임(2차원 데이터)
df = pd.read_csv('credit.csv')
# print(df)
 
# 나이 평균을 내보자.
# print(df['나이'].mean()) # 평균
# print(df['나이'].mode()) # 최빈값
# print(df['나이'].max())
# print(df['나이'].min())
# print(df['나이'].describe())

print(df.groupby("성별").mean())

print(df[['나이','사용금액']].corr())# 관계도 출력 0.1만큼 비례한다. 1에 가까울수록 비례함.

print( df[df['나이']> 50 ])
print(df.query("나이 > 50 and 기혼 == 'Married'"))# 여러 조건을 넣을때 / 컬럼은 ''안씀. 문자만 씀

셔츠 = [15, 20, 25]
바지 = [150, 100, 150] #list를 dataframe으로 변환 -> 분석하기 편함.

딕셔너리 = {
    '셔츠' : [15, 20, 25],
    '바지' : [150, 100, 150]
}
df2 = pd.DataFrame(딕셔너리)
print(df2)

# 남자이면서 결혼한 사람이 남자,싱글인 사람보다 사용금액이 평균적으로 높을까?
print("남자이면서 결혼한 사람이 남자,싱글인 사람보다 사용금액이 평균적으로 높을까?")
merried_man = df.query("성별 == 'M' and 기혼 == 'Married'")
single_man = df.query("성별 == 'M' and 기혼 == 'Single'")
print(merried_man.mean())
print(single_man.mean())


# 연간 소득이 높을수록 사용금액이 높을까?
print("연간 소득이 높을수록 사용금액이 높을까?")
print(df.groupby("소득").mean()) # corr 할라했는데 소득이 문자라서 안됨;
