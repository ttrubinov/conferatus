import matplotlib

from raytracing.Fourier import Fourier
from raytracing.Dataset import Dataset, Sample
from raytracing.Plotter import Plotter
from raytracing.ArduinoController import ArduinoController

from ui.RecordingPresenter import RecordingPresenter
from ui.UserDefinedParamerers import UserDefinedParameters
from PyQt6 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

matplotlib.use('Qt5Agg')

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class Plotter(QtWidgets.QDialog):
    def __init__(self):
        super(Plotter, self).__init__()

        sc = MplCanvas(self, width=5, height=4, dpi=90)
        sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(sc)

        self.setLayout(layout)

        # layout = QtWidgets.QVBoxLayout()
        # layout.addWidget(sc)

        # # Create a placeholder widget to hold our toolbar and canvas.
        # widget = QtWidgets.QWidget()
        # widget.setLayout(layout)
        # self.setCentralWidget(widget)
        # self.show()


class RecordingThread(QtCore.QThread):
    def __init__(self, recordingPresenter, params : UserDefinedParameters, parent=None):
        super(RecordingThread, self).__init__(parent)
        self.__recordingPresenter__ = recordingPresenter
        self.__params__ = params
        
    def run(self):
        Plotter().exec()

        with ArduinoController(batch_size = self.__params__.batchSize, port = self.__params__.port) as arduinoController:
            data = arduinoController.recordData()

        for i in range(0, self.__params__.batchSize):
            fourierSample = Fourier.get_amplitudes_and_phases(data[i])
            Plotter().show()
            # Plotter.draw(y_axis=fourierSample, color = ['red', 'blue', 'green'])
            # if self.__recordingPresenter__.processSampleDialog():
            #     badData = False 
            # else:
            #     badData = True



            sample = Sample(signals = fourierSample, 
                            angle = self.__params__.angle, 
                            bad_data = not self.__recordingPresenter__.processSampleDialog(),
                            frequency = self.__params__.frequency,
                            person = self.__params__.person)

            Dataset.addData(sample, file_path=self.__params__.filename)
        Dataset.saveData(sync = True, file_path = self.__params__.filename)
            
            


class RecordingModel:
    def __init__(self, recordingPresenter : RecordingPresenter):
        self.__recordingPresenter__ = recordingPresenter

    def readSamples(self, params : UserDefinedParameters):
        print(params)

        self.thread = RecordingThread(self.__recordingPresenter__, params)
        self.thread.finished.connect(self.__recordingPresenter__.finishedReadingSamples)

        self.thread.start()
