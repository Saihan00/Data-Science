import tensorflow as tf
from tensorflow import keras
import numpy as np

model = keras.sequential(
    [
        keras.layer.Dense(unit=1,
         input_shape=(1))
    ]
)

model.compile(optimizer='sgd' ,
loss='mean_squared_error')

x = np.array([1,2,3,4,6,5])
y = np.array([4,5,8,98,20])

model.fit(x,y,epoch=4)

print(model.predict([10]))