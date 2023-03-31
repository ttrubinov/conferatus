import numpy as np
from scipy.fft import fft, fftfreq


class Fourier:
    def __init__(self, array: list[list[float]]):
        self.array = array

    def fft(self):
        return list(map(lambda x: fft(np.array(x)), self.array))

    def fft_freq(self, sampleSpacing=1 / 12000):
        n = len(self.array)
        return fftfreq(n, sampleSpacing)[:n // 2]
