import numpy as np
# from keras import Sequential
# from keras.layers import Dense
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers


class Model:

    def __init__(self, sample_size=250, mic_amount=3):
        inputs = keras.Input(shape=(784,), name="digits")
        x = layers.Dense(64, activation="relu", name="dense_1")(inputs)
        x = layers.Dense(64, activation="relu", name="dense_2")(x)
        outputs = layers.Dense(10, activation="softmax", name="predictions")(x)

    pass


# x = np.arange(0, 10, 0.2, dtype=float)
# y = x > 5 + 0
# X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.75)
# print(X_test, X_train, y_test, y_train)
#
# model = keras.Sequential([
#     layers.Dense(4, input_dim=1, activation='relu'),
#     layers.Dense(5, activation='relu'),
#     layers.Dense(1, activation='sigmoid')
# ])

inp = np.array([[1, 0, 0], [1, 0, 0], [1, 0, 0]])
model = keras.Sequential()
model.add(keras.Input(shape=3))
model.add(layers.Dense(2, activation="relu"))
print(model.summary())
print(model(inp))

# model.compile(loss='binary_crossentropy', optimizer='adam', jit_compile=True)
# history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=2000, batch_size=10)
