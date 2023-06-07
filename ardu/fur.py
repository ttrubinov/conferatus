import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq
# Number of sample points
N = 600
# sample spacing
T = 1 / 11000
# x = np.linspace(0.0, N*T, N, endpoint=False)
#
# y = np.sin(50.0 * 2.0*np.pi*x) + 2*np.sin(30.0 * 2.0*np.pi*x) + 0*0.25*np.sin(25.0 * 2.0*np.pi*x)
data = [[], [], []]
with open("oldSamples/sample3.txt", mode="r") as f:
    s = f.readline()
    nn = 100
    counter = 0
    while True:
        s = f.readline()
        if "End" in s:
            break
        if counter % nn == 0:
            for i in data:
                i.append([])
        s = s.split()
        for i in range(0, 3):
            data[i][counter // nn].append(float(s[i]))
        counter += 1


def fastFour(arr):
    y = np.array(arr)
    yf = fft(y)
    return yf


def plotter(arr_ff, num, title):
    def plotter_one(arr_f, color):
        n = len(arr_f)
        xf = fftfreq(n, T)[:n // 2]
        plt.plot(xf[1:n // 2], 2.0 / n * arr_f[1:n // 2],
                 # 'o',
                 color=color)

    plt.legend(['FFT', 'FFT'])

    for micrArr, col in zip(arr_ff, np.array(["red", "green", "blue"])):
        plotter_one(micrArr, col)
    plt.title(title)
    #plt.xlim(0, 1000)
    plt.grid()
    plt.show()
    plt.clf()


def getAmplitudes_Angles(dataFour):
    return np.abs(dataFour), np.angle(dataFour)


for i in range(len(data[0])):
    amplitudes, phases = getAmplitudes_Angles(
        np.array([fastFour(data[0][i]), fastFour(data[1][i]), fastFour(data[2][i])]))
    plotter(amplitudes, i, f"amplitudes {i}")
    plotter(phases, i, "phases")
