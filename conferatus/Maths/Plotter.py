from matplotlib import pyplot as plt
import matplotlib
from scipy.fft import fftfreq

matplotlib.use('Agg')


class Plotter:
    @staticmethod
    def draw(y_axis: list[list[float]], x_axis: list[float] = None, color: list[str] = None, name: str = None,
             x_lim: int = 2000, legend: str = None, file_path: str = 'Maths/plot/fig.png') -> None:
        def __show(plotTitle: str = ""):
            plt.title(plotTitle)
            if x_lim is not None:
                plt.xlim(0, x_lim)
            if legend is not None:
                plt.legend(legend)
            plt.grid()
            plt.savefig(file_path, dpi=150)
            plt.clf()

        def __x_axis_filling():
            if x_axis is None:
                n = len(y_axis[0])
                return fftfreq(n, 1 / 11050)[1:n // 2]
            else:
                return x_axis

        if color is not None and len(y_axis) == len(color):
            for data, clr in zip(y_axis, color):
                x_axis = __x_axis_filling()
                plt.plot(x_axis, data[1:len(data) // 2], color=clr)
        else:
            for data in y_axis:
                x_axis = __x_axis_filling()
                plt.plot(x_axis, data[1:len(data) // 2], color="b")
        if name is not None:
            __show(name)
        else:
            __show()
