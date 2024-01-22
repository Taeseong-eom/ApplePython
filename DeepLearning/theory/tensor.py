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
    
텐서1 = tf.constant([1,2,3]) # 이걸 왜쓸까? 행렬끼리 연산을 하기 위해서 사용함.
텐서2 = tf.constant([4,5,6])
print(텐서1 + 텐서2)
텐서3 = tf.constant([[1,2],
                    [3,4]])

print(tf.add(텐서1,텐서2))

#행렬의 곱은
# tf.matmul(텐서1,텐서2) # 이렇게 하면 됨.

텐서4 = tf.zeros([2,2,3]) 
print(텐서1.shape) # 뒤에서부터 0이 3개 담긴 리스트를 2개 만들고 그걸 또 2개 만들어라.

# constant 하면 변하지 않는 상수가 되고 Variable로 하면 변수로 선언됨
w = tf.Variable(1.0)
print(w) #값은 numpy에 있어서 numpy를 출력해야함.
print(w.numpy())
w.assign(2) # 변수 수정
print(w)