import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np



import multiprocessing


# 의류 이미지를 보고 종류를 분류하는 ai
    
# 사진을 어떻게 뉴럴 네트워크에 넣을 수 있을까 ? 
# 숫자로 바꿔서 넣어야한다.
    
# 이미지를 확대하면 픽셀로 구성되어 있다.
# 각각의 픽셀의 RGB 값들을 뉴럴 네트워크에 넣으면 된다. 단 , 흑백은 한가지 값임.
 
#그래서 더 쉬운 흑백사진으로 학습을 시켜보자.

(trainX,trainY),(testX, testY) = tf.keras.datasets.fashion_mnist.load_data() # (학습데이터, 정답), (테스트 데이터, 테스트 정답)


#이미지 데이터 전처리 0 ~ 255를 0 ~ 1로 압축해서 넣을 수 있음 -> 선택사항임
trainX = trainX / 255.0
testX = testX / 255.0

 
trainX = trainX.reshape((trainX.shape[0],28,28,1))
testX = testX.reshape((testX.shape[0],28,28,1))


# print(trainX[0])
# print(trainX.shape) #(60000, 28, 28) 28*28개가 60000개 있다. 데이터가 6만개

# print(trainY)

# plt.imshow(trainX[1]) # 미리 이미지를 보고 싶을 경우에 사용
# plt.gray() # 흑백으로 보고 싶을때 
# plt.colorbar()
# plt.show()

class_names = ['T-shirt/top','Trouser','Pullover','Dress''Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']

model = tf.keras.Sequential([ #activation='relu' 양수만 뱉어 내는데 이미지는 음수가 나올 수 없으니 사용
  #convolution 적용
  tf.keras.layers.Conv2D(32, (3,3),padding="same",activation='relu',input_shape=(28,28,1)), # 32개의 이미지 복사본(특징들) 생성해줘.//(3,3)-> 커널 사이즈(알아서 하면됨)// padding="same" -> 컨볼루션 하면 크기가 작아지는데 똑같이 유지해줌(테투리 1픽셀 추가)
  # input_shape=(28,28,1) 기존 데이터는 [[...],[...]] 이렇게 되어있는데 Conv 하려면 [[.][.]] 로 바꿔줘야 해서 모양 지정. -> 컬러일땐 당연히 3
  
  #pooling 을 통해 가운데로 모으자
  tf.keras.layers.MaxPooling2D( (2,2)), # (2,2) 사이즈로 줄일거임

  # tf.keras.layers.Dense(128,input_shape=(28,28),activation='relu'), #relu : 음수는 다 0으로 만들어줌 // convolution layer에서 자주씀
  tf.keras.layers.Flatten(), # 순서를 바꿔줘야함.
  tf.keras.layers.Dense(64,activation='relu'),
  #
  tf.keras.layers.Dense(10,activation='softmax') # 10개의 확률을 뱉게함
]) #확률로 압축하고 싶을때 sigmoid, softmax가 있다.
# sigmoid는 0,1 두 가지 로 구분할때 사용하고 // 마지막 레이어는 1로 설정함.
# softmax는 여러 카테고리 중에서 어떤 카테고리 확률이 높을지에 사용// 총합이 1이 나옴.

model.summary() # 데이터 넣어서 학습 시키기 전에 한번 model 아웃라인을 보고 싶을때 사용
#단 위에 input_shape을 지정해줘야한다.(하나의 데이터 모양으로)
#  Layer (type)                Output Shape              Param #
# =================================================================
#  dense (Dense)               (None, 28, 128)           3712

#  dense_1 (Dense)             (None, 28, 64)            8256

#  dense_2 (Dense)             (None, 28, 10)            650

# =================================================================
# 이렇게 데이터가 2차원 데이터로 나오는데 일차원으로 보고 싶으니까 tf.keras.layers.Flatten() -> 일차원으로 압축 을 해준다.
# _________________________________________________________________
#  Layer (type)                Output Shape              Param #
# =================================================================
#  dense (Dense)               (None, 28, 128)           3712 <- 학습 가능한 w값 개수

#  dense_1 (Dense)             (None, 28, 64)            8256

#  flatten (Flatten)           (None, 1792)              0

#  dense_2 (Dense)             (None, 10)                17930

# =================================================================


#loss함수에는 3가지 정도 있고
model.compile(loss="sparse_categorical_crossentropy",optimizer='adam',metrics=['accuracy']) #categorical_crossentoropy 여러 카테고리를 확률로 예측하고 싶을때 사용
# 답안(Y데이터)이 원핫인코딩되어 있으면 categorical_crossentropy을 사용하고
#정수(0,1,2,3)로 되어 있으면 sparse_categorical_crossentropy 사용한다.

model.fit(trainX,trainY,validation_data=(testX,testY),epochs=5)

# 지금은 2차원 데이터를 1차원 데이터로 변환하여 학습을 하였다.
# 이 경우 데이터가 수정되면 제대로 분류를 못하는 문제가 생긴다.

# 그래서 2차원 그대로 인식할 수 있게 하기 위해서 convolution을 해야한다. -> 하나의 데이터에서 특징을 여러개 뽑아 복사해서 저장. --> CNN
# 이 것을 학습하면 정확도가 올라간다

# 단, 이 경우에도 사물의 위치에 따라 잘못 학습 및 인식을 할 수 있기 때문에 pooling layer를 사용해야한다. -> 색상의 값을 평균, 맥스 등등으로 축소를 하면 사물의 특징을 중간으로 몰 수 있다.

# 학습이 잘 되었는지 확인해보자.
score = model.evaluate(testX,testY) # 학습 못했던 테스트 데이터를 넣으면 됨.
print(score)

# loss: 0.1816 - accuracy: 0.9338 인데 
# 실제 test에 대한 점수는 [0.25358477234840393, 0.9096999764442444] 이다. 순서대로 loss, accuracy인데
# 학습데이터를 외워서 그럼; -> overfitting

# 이걸 해결하기 위해서는 epoch 한번 할 떄마다 채점하면 되지 않을까?
# model.fit(trainX,trainY,validation_data=(testX,testY),epochs=5)
# 이렇게 validation_data 하면됨. epochs를 100 이런식으로 하고 반복하다가 만족할만한 val_accuracy나오면 학습 멈추면 됨 그래야 오버피팅이 안나옴
# 어떻게 하면 accuracy이 높아질지 Dense나 convolution+pooling를 추가하면서 테스트 하면 됨