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
    
# 키 = [170, 180, 175, 160]
# 신발 = [260, 270, 265, 255]

# y(신발) = ax(키) + b
# 키와 신발사이즈가 연관이 있을 거 같아서 식을 세움.
키 = 170
신발 = 260

a = tf.Variable(0.1)
b = tf.Variable(0.2)

def 손실함수():
  실제값 = 260
  예측값 = 키 * a + b
  return tf.square(실제값 - 예측값) # (오차) .square 하면 제곱해줌.

opt = tf.keras.optimizers.Adam(learning_rate=0.1) # 경사하강법을 해서 w를 업데이트 해줌. adam 등등 여러가지. learning_rate=하면 w를 얼만큼씩 수정할지.

for i in range(300): # 경사하강 300번
    opt.minimize(손실함수, var_list=[a,b]) # 경사하강법 시작. (손실함수, var_list(??,??) <- 업데이트할 변수들) 
    print(a.numpy(),b.numpy())