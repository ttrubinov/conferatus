from matplotlib import pyplot as plt

from conferatus.confertus.raytracing.Fourier import Fourier


class Plotter:
    def draw(self, arrY: list[list[float]], arrX: list[float] = None, color: list[str] = None, name: list[str] = None,
             xlim: int = None, legend: str = None):
        def show(plotTitle: str = ""):
            plt.title(plotTitle)
            if xlim is not None:
                plt.xlim(0, xlim)
            if legend is not None:
                plt.legend(legend)
            plt.grid()
            plt.show()
            plt.clf()

        def arr_filling():
            if arrX is None:
                n = len(arrY)
                fourier = Fourier(arrY)
                return fourier.fft_freq()[1:n // 2]
            else:
                return arrX

        if color is not None and name is not None and len(arrY) == len(color) == len(name):
            for data, clr, title in zip(arrY, color, name):
                arrX = arr_filling()
                plt.plot(arrX, data, color=clr)
                show(title)
        else:
            for data in arrY:
                arrX = arr_filling()
                plt.plot(arrX, data, color="b")
                show()
