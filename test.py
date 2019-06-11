
#
# import keras
#
#
# print(keras.backend.backend())
# from keras import backend as K
#
# inputs = K.placeholder(shape=(2, 4, 5))
# # also works:
# inputs = K.placeholder(shape=(None, 4, 5))
# # also works:
# inputs = K.placeholder(ndim=3)
#
#
# import numpy as np
# val = np.random.random((3, 4, 5))
# var = K.variable(value=val)
#
# # all-zeros variable:
# var = K.zeros(shape=(3, 4, 5))
# # all-ones:
# var = K.ones(shape=(3, 4, 5))
#
#
# # Initializing Tensors with Random Numbers
# b = K.random_uniform_variable(shape=(3, 4), low=0, high=1) # Uniform distribution
# c = K.random_normal_variable(shape=(3, 4), mean=0, scale=1) # Gaussian distribution
# d = K.random_normal_variable(shape=(3, 4), mean=0, scale=1)
#
# # Tensor Arithmetic
# a = b + c * K.abs(d)
# c = K.dot(a, K.transpose(b))
# a = K.sum(b, axis=1)
# a = K.softmax(b)
# a = K.concatenate([b, c], axis=-1)
# etc...
if __name__ == '__main__':
    print("ok")
    print()
