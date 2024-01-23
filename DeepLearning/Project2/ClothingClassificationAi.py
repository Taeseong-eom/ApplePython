import tensorflow as tf
import matplotlib.pyplot as plt


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

# 의류 이미지를 보고 종류를 분류하는 ai
    
# 사진을 어떻게 뉴럴 네트워크에 넣을 수 있을까 ? 
# 숫자로 바꿔서 넣어야한다.
    
# 이미지를 확대하면 픽셀로 구성되어 있다.
# 각각의 픽셀의 RGB 값들을 뉴럴 네트워크에 넣으면 된다. 단 , 흑백은 한가지 값임.
 
#그래서 더 쉬운 흑백사진으로 학습을 시켜보자.
    
(trainX,trainY),(testX, testY) = tf.keras.datasets.fashion_mnist.load_data() # (학습데이터, 정답), (테스트 데이터, 테스트 정답)

# print(trainX[0])
# print(trainX.shape) #(60000, 28, 28) 28*28개가 60000개 있다. 데이터가 6만개

# print(trainY)

# plt.imshow(trainX[1]) # 미리 이미지를 보고 싶을 경우에 사용
# plt.gray() # 흑백으로 보고 싶을때 
# plt.colorbar()
# plt.show()

class_names = ['T-shirt/top','Trouser','Pullover','Dress''Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']

model = tf.keras.Sequential([
  tf.keras.layers.Dense(128,input_shape=(28,28),activation='relu'), #relu : 음수는 다 0으로 만들어줌 // convolution layer에서 자주씀
  tf.keras.layers.Dense(64,activation='relu'),
  tf.keras.layers.Flatten(),
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

model.fit(trainX,trainY,epochs=5)




