import numpy as np
from scipy.fft import fft, fftfreq


class Fourier:
    def __init__(self, array):
        self.array = array

    def fft(self):
        return fft(np.array(self.array))

    def fft_freq(self, sampleSpacing=1 / 12000):
        n = len(self.array)
        return fftfreq(n, sampleSpacing)[:n // 2]
