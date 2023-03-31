import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
# from keras import Sequential
# from keras.layers import Dense
from sklearn.model_selection import train_test_split


class Model:
    pass


x = np.arange(0, 10, 0.2, dtype=float)
y = x > 5 + 0
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.75)
print(X_test, X_train, y_test, y_train)

model = keras.Sequential([
    layers.Dense(4, input_dim=1, activation='relu'),
    layers.Dense(5, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])
model = keras.Sequential()
model.add(keras.Input(shape=(4,)))
model.add(layers.Dense(2, activation="relu"))

model.summary()


# model.compile(loss='binary_crossentropy', optimizer='adam', jit_compile=True)
# history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=2000, batch_size=10)
