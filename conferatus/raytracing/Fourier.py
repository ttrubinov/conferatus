import numpy as np
from numpy import ndarray
from scipy.fft import fft, fftfreq


class Fourier:
    @staticmethod
    def fft(array: list[list[float]], result_size: int = 250) -> list[list[complex]]:
        return list(map(lambda data: fft(np.array(data))[:result_size], array))

    @staticmethod
    def fft_freq(array: list[list[float]], sampleSpacing: float = 1 / 12000) -> list[list[complex]]:
        return list(map(lambda data: fftfreq(len(data), sampleSpacing)[:len(data) // 2], array))

    @staticmethod
    def get_amplitudes_and_phases(data: list[list[float]],
                                  whether_to_calculate_phases: bool = False) -> (ndarray, ndarray):
        fft_res = fft(data)
        if whether_to_calculate_phases:
            return np.abs(fft_res), np.angle(fft_res)
        else:
            return np.abs(fft_res)
