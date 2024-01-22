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

#딥러닝으로 추론해서 답을 맞춰보자.
train_x = [1,2,3,4,5,6,7]
train_y = [3,5,7,9,11,13,15]

a = tf.Variable(0.1)
b = tf.Variable(0.1) # 초기값은 랜덤하게 넣음



def 손실함수(a,b): #손실함수에서 뭘 뱉을지에 따라 다양하게 적용하면 됨 정수인 경우엔 mean squared error, 확률같은 경우엔 cross entropy 등..
  예측_y = train_x * a + b
  return tf.keras.losses.mse(train_y, 예측_y)

opt = tf.keras.optimizers.Adam(learning_rate=0.01) # 경사하강법을 해서 w를 업데이트 해줌. adam 등등 여러가지. learning_rate=하면 w를 얼만큼씩 수정할지.

for i in range(2900): # 경사하강 300번
    opt.minimize(lambda:손실함수(a,b), var_list=[a,b]) # 경사하강법 시작. (손실함수, var_list(??,??) <- 업데이트할 변수들) 
    print(a.numpy(),b.numpy())






