from matplotlib import pyplot as plt


class Plotter:
    def draw(self, arrX: list[float], arrY: list[list[float]], color: list[str] = None, name: list[str] = None,
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

        if color is not None and name is not None and len(arrY) == len(color) == len(name):
            for data, clr, title in zip(arrY, color, name):
                plt.plot(arrX, data, color=clr)
                show(title)
        else:
            for data in arrY:
                plt.plot(arrX, data, color="b")
                show()
