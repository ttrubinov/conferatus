import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq

# Number of sample points
N = 600
# sample spacing
T = 1.0 / 700.0
T = 1/1400
# x = np.linspace(0.0, N*T, N, endpoint=False)
#
# y = np.sin(50.0 * 2.0*np.pi*x) + 2*np.sin(30.0 * 2.0*np.pi*x) + 0*0.25*np.sin(25.0 * 2.0*np.pi*x)
data = [[], [], []]
with open("sample106.txt", mode="r") as f:
    s = f.readline()
    counter = 0
    while True:
        s = f.readline()
        if "End" in s:
            break
        if counter % 100 == 0:
            for i in data:
                i.append([])
        s = s.split()
        for i in range(0, 3):

            data[i][counter // 100].append(float(s[i]))
        counter += 1

print(len(data[1]))
print(*data[1], sep="\n")
print(data)


def fastFour(arr):
    y = np.array(arr)
    yf = fft(y)
    return yf


def plotter(arr_ff, num):
    n = len(arr_ff)
    xf = fftfreq(n, T)[:n // 2]
    plt.semilogy(xf[1:n // 2], 2.0 / n * np.abs(arr_ff[1:n // 2]), '-b')
    plt.legend(['FFT', 'FFT'])
    plt.title(f"{num}")
    plt.grid()
    plt.show()
    plt.clf()


for i in range(len(data[1])):
    farr = fastFour(data[1][i])
    plotter(farr, i)


def smth():
    arr = []
    arr2 = []
    for i in range(0, 100):
        x = i / 100
        y = (i + np.pi) / 12.5
        arr.append(5 * np.sin(2 * np.pi * x) + 5 * np.sin(2 * np.pi * y))
        x *= 2
        y = x * 4
        arr2.append(3 * np.sin(2 * np.pi * x) + 2 * np.sin(2 * np.pi * y))
    # arr = [5, 1, 6, 2, 1, 3]
    N = len(arr)
    y = np.array(arr)
    yf = fft(y)
    y2 = np.array(arr2)
    yf2 = fft(y2)

    xf = fftfreq(N, T)[:N // 2]
    print(xf, "\n\n\n")
    print(2.0 / N * np.abs(yf[1:N // 2]), "\n", 2.0 / N * np.abs(yf2[1:N // 2]))
