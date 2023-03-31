import numpy as np
from scipy.fft import fft, fftfreq


class Fourier:
    def __init__(self, array: list[list[float]]):
        self.array = array

    def fft(self):
        return list(map(lambda data: fft(np.array(data)), self.array))

    def fft_freq(self, sampleSpacing=1 / 12000):
        return list(map(lambda data: fftfreq(len(data), sampleSpacing)[:len(data) // 2], self.array))
