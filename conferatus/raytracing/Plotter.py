from matplotlib import pyplot as plt

from conferatus.conferatus.raytracing.Fourier import Fourier


class Plotter:
    @staticmethod
    def draw(y_axis: list[list[float]], x_axis: list[float] = None, color: list[str] = None, name: list[str] = None,
             x_lim: int = None, legend: str = None):
        def show(plotTitle: str = ""):
            plt.title(plotTitle)
            if x_lim is not None:
                plt.xlim(0, x_lim)
            if legend is not None:
                plt.legend(legend)
            plt.grid()
            plt.show()
            plt.clf()

        def x_axis_filling():
            if x_axis is None:
                n = len(y_axis)
                return Fourier.fft_freq(y_axis)[1:n // 2]
            else:
                return x_axis

        if color is not None and name is not None and len(y_axis) == len(color) == len(name):
            for data, clr, title in zip(y_axis, color, name):
                x_axis = x_axis_filling()
                plt.plot(x_axis, data, color=clr)
                show(title)
        else:
            for data in y_axis:
                x_axis = x_axis_filling()
                plt.plot(x_axis, data, color="b")
                show()
