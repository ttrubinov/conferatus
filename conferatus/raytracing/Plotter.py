from matplotlib import pyplot as plt
import matplotlib
matplotlib.use("Agg")

from scipy.fft import fftfreq

class Plotter:
    @staticmethod
    def draw(y_axis: list[list[float]], x_axis: list[float] = None, color: list[str] = None, name: list[str] = None,
             x_lim: int = None, legend: str = None) -> None:
        def __show(plotTitle: str = ""):
            plt.title(plotTitle)
            if x_lim is not None:
                plt.xlim(0, x_lim)
            if legend is not None:
                plt.legend(legend)
            plt.grid()
            plt.show()
            plt.clf()

        def __x_axis_filling():
            if x_axis is None:
                n = len(y_axis[0])
                return fftfreq(n, 1 / 12000)[:len(data) // 2]
            else:
                return x_axis

        if color is not None and name is not None and len(y_axis) == len(color) == len(name):
            for data, clr, title in zip(y_axis, color, name):
                x_axis = __x_axis_filling()
                plt.plot(x_axis, data, color=clr)
                __show(title)
        else:
            for data in y_axis:
                x_axis = __x_axis_filling()
                plt.plot(x_axis, data, color="b")
                __show()
