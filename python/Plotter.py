from matplotlib import pyplot as plt


class Plotter:
    def show(*args, xlim=None, legend=None, title="", color="black"):
        plt.plot(args, color)
        plt.title(title)
        if xlim is not None:
            plt.xlim(0, xlim)
        if legend is not None:
            plt.legend(legend)
        plt.grid()
        plt.show()
        plt.clf()
