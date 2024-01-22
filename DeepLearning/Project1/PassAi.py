import pandas as pd
import numpy as np

# 데이터 불러오기
data = pd.read_csv(r'C:\Users\taeseong\Desktop\파이썬\DeepLearning\Project1\gpascore.csv')

# 데이터에 빈칸이 있는지 확인
print(data.isnull().sum())

# 데이터 전처리(가공)
data = data.dropna() # 빈칸 삭제 // 다른걸 넣을 수도 있음

y데이터 = data['admit'].values
x데이터 = []

for i,rows in data.iterrows(): # dataframe이라 iterrows 가능 (한 행씩 실행가능)
  x데이터.append([ rows['gre'], rows['gpa'], rows['rank'] ])





import tensorflow as tf


gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
  try:
    # Currently, memory growth needs to be the same across GPUs
    for gpu in gpus:
      tf.config.experimental.set_memory_growth(gpu, True)
    logical_gpus = tf.config.experimental.list_logical_devices('GPU')
    print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
  except RuntimeError as e:
    # Memory growth must be set before GPUs have been initialized
    print(e)

# 대학 합격 여부 판별 ai

model = tf.keras.models.Sequential([ # t
  tf.keras.layers.Dense(64, activation='tanh'), # (노드의 개수) 맘대로 정하면 됨 결과가 잘나오게 // activation(활성함수)를 넣어줘야하는데 sigmoid, tanh, relu 등등 원하는 거 넣기
  tf.keras.layers.Dense(128, activation='tanh'), # 관습적으로 2의 제곱수로 해둠
  tf.keras.layers.Dense(1, activation='sigmoid') # 마지막은 하나의 노드여야함. 왜? 결과가 하나여야 하니까 -> 원하는 출력 개수만큼 마지막 레이어 수를 조절해여함.
]) # sigmoid 는 0 ~ 1 사이 값을 뱉어서 확률을 알 수 있음. 
# Sequential 쓰면 신경망 레이어들 만들어줌(딥러닝 모델)

# 딥러닝에서 정수 예측은 힘듬

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy']) # optimizer: w값을 얼만큼씩 조절할지, loss 에는 적당히 맞게 쓰면 되는데 확률은 binary_crossentropy가 좋음
# metrics 어떤 요소로 평가할건지.

model.fit(np.array(x데이터), np.array(y데이터) ,epochs=1000) # x데이터(학습데이터), y데이터(결과) , epochs(몇번 학습할지)를 넣으면 됨
# 단, 학습 데이터를 넣을 때 리스트로 바로 넣으면 안되고 numpy나 tensor로 넣어야함.

# loss 손실의 총합 (작을 수록 좋음)
# accuracy: 얼마나 예측이 잘맞는지 (높을수록 좋음)
# accuracy: 0.7741 나왔다.

# 이제 예측을 해보자.
예측값 = model.predict([[750, 3.50, 3],[400, 2.2 , 1]])
print(예측값)

# [[0.68894345]
# [0.01693512]]
