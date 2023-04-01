import numpy as np
from numpy import ndarray
from scipy.fft import fft, fftfreq


class Fourier:
    @staticmethod
    def fft(array: list[list[float]], result_size: int = 250) -> list[list[complex]]:
        return list(map(lambda data: list(fft(np.array(data))[:result_size]), array))

    @staticmethod
    def fft_freq(array: list[list[float]], sampleSpacing: float = 1 / 11050) -> list[list[complex]]:
        return list(map(lambda data: fftfreq(len(data), sampleSpacing)[:len(data) // 2], array))

    @staticmethod
    def get_amplitudes_and_phases(data: list[list[float]],
                                  should_calculate_phases: bool = False) -> tuple[list, list] | list:
        fft_res = Fourier.fft(data)
        if should_calculate_phases:
            return list(map(list, np.abs(fft_res))), list(map(list, np.angle(fft_res)))
        else:
            return list(map(list, np.abs(fft_res)))

