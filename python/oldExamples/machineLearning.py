import random

import matplotlib.pyplot as plt
import numpy as np
from keras import Sequential
from keras.layers import Dense
from scipy.fft import fft, fftfreq
from sklearn.model_selection import train_test_split


def randK(start=0.8, end=1.25):
    return random.random() * (end - start) + start


# from sklearn.preprocessing import OneHotEncoder
# Neural network

x = np.arange(0, 10, 0.2, dtype=float)
y = x > 5 + 0
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.75)
print(X_test, X_train, y_test, y_train)

model = Sequential()
model.add(Dense(30, input_dim=1, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', jit_compile=True)
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=2000, batch_size=10)

print(model.predict(np.array([0.0, 1.0, 2.0])))
print(model.predict(np.array([6.0, 9.0, 5.5])))


def mySin(value, amplitude, freq):
    return np.sin(value * 2 * np.pi * freq) * amplitude


def blurMySin(value, amplitude, freq, num, bias):
    res = 0
    for fr in np.linspace(freq - bias, freq + bias, num):
        res += mySin(value, amplitude * (1 - 0 * np.abs(freq - fr) / (bias * 3)), fr) * randK(0.8, 1.25)
    return res / num


N = 200
T = 1 / 1000
voice1_inp = np.linspace(0.0, N * T, N, endpoint=False)
print(voice1_inp, end="\n\n")
voice1_out = randK() * 50 * np.sin(150.0 * 2.0 * np.pi * voice1_inp) + randK() * 75 * np.sin(
    300.0 * 2.0 * np.pi * voice1_inp) \
             + 30 * np.sin(400 * 2.0 * np.pi * voice1_inp) * randK()

voice1_out = blurMySin(voice1_inp, randK() * 80, 150, 5, 2) + blurMySin(voice1_inp, randK() * 70, 350, 5, 3) \
             + blurMySin(voice1_inp, randK() * 50, 425, 4, 4)
print(voice1_out, end="\n\n")

vf = np.vectorize(lambda x: x * randK(0.5, 2))
error = np.array([randK(-15, 15) for i in range(N)])
print(error, end="\n\n")


def plotter(arr_ff, num, title):
    plt.legend(['FFT', 'FFT'])
    n = len(arr_ff)
    xf = fftfreq(n, T)[:n // 2]
    plt.plot(xf[1:n // 2], 2.0 / n * arr_ff[1:n // 2],
             # 'o',
             color="green")
    plt.title(title)
    # plt.xlim(0, 1 / T)
    plt.grid()
    plt.show()
    plt.clf()


def getAmplitudes_Angles(dataFour):
    return np.abs(dataFour), np.angle(dataFour)


# print(voice1_out + error*0)
signal_out = voice1_out + error
fur_out = fft(signal_out)
# plotter(np.abs(fur_out), 1, f"voice")
plotter(np.abs(fur_out), 1, f"voice")
