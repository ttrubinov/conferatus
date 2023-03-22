import json
import time

import matplotlib.pyplot as plt
import numpy as np
import serial
from scipy.fft import fft, fftfreq


def getConfig():
    try:
        with open("config.txt", "r") as f:
            dct = json.load(f)
            print(dct)
    except FileNotFoundError:
        dct = dict()
        dct["last"] = 0
        with open("config.txt", "w") as f:
            print(json.dumps(dct), file=f)
    return dct


T = 1 / 11000
data = [[], [], []]


# make sure the 'COM#' is set according the Windows Device Manager
def fastFour(arr):
    y = np.array(arr)
    yf = fft(y)
    return yf


def plotter_one(arr_f, color):
    n = len(arr_f)
    xf = fftfreq(n, T)[:n // 2]
    plt.plot(xf[1:n // 2], 2.0 / n * arr_f[1:n // 2],
             color=color)


def plotter(arr_ff, title):
    plt.legend(['FFT', 'FFT'])

    for micrArr, col in zip(arr_ff, np.array(["red", "green", "blue"])):
        plotter_one(micrArr, col)
    plt.title(title)
    plt.xlim(0, 2000)
    plt.grid()
    plt.show()
    plt.clf()


def getSerialData():
    arr = []
    with serial.Serial('COM4', 115200, timeout=1) as ser:
        time.sleep(3)
        ser.write(b'init')
        print("Started")
        for i in range(0, 100):
            temporary = [[], [], []]
            for j in range(1000):
                line = ser.readline()  # read a byte
                if line:
                    string = list(map(float,
                                      line.decode().strip().split()))  # convert the byte string to a unicode string
                    for k, val in enumerate(string):
                        temporary[k].append(val)
            print(temporary)
            ser.write(b'stop')
            resFur = list(map(fastFour, temporary))
            print(list(map(len, temporary)))
            print(resFur)
            plotter(resFur, f"title{i}")
            ser.write(b'continue')
    return arr


def saveData(dct, arr):
    lst = dct["last"]
    with open(f"sample{lst}.txt", "w") as outputFile:
        print(*arr, "End", sep="\n", file=outputFile)

    dct["last"] = dct["last"] + 1
    with open("config.txt", "w", encoding='utf-8') as f:
        print(json.dumps(dct), file=f)


def main():
    dct = getConfig()
    arr = getSerialData()
    saveData(dct, arr)


if __name__ == '__main__':
    main()
