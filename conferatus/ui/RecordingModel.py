from Maths.Fourier import Fourier
from ML.Datasets.Dataset import Dataset, Sample
from Maths.Plotter import Plotter
from Arduino.ArduinoController import ArduinoController

from ui.RecordingPresenter import RecordingPresenter
from ui.UserDefinedParamerers import UserDefinedParameters
from PyQt6 import QtCore


class RecordingThread(QtCore.QThread):
    def __init__(self, recordingPresenter, params : UserDefinedParameters, parent=None):
        super(RecordingThread, self).__init__(parent)
        self.__recordingPresenter__ = recordingPresenter
        self.__params__ = params

    def run(self):
        with ArduinoController(batch_size = self.__params__.batchSize, port = self.__params__.port) as arduinoController:
            self.__data = arduinoController.recordData()

    def data(self):
        return self.__data


class RecordingModel:
    def __init__(self, recordingPresenter : RecordingPresenter):
        self.__recordingPresenter__ = recordingPresenter

    def readSamples(self, params : UserDefinedParameters):
        print(params)

        self.__thread = RecordingThread(self.__recordingPresenter__, params)
        self.__thread.finished.connect(self.__finishedReadingSamples)
        self.__thread.start()

    def __finishedReadingSamples(self):
        self.selectSamples(self.__thread.data())
        self.__recordingPresenter__.finishedReadingSamples()

    def selectSamples(self, data):
        samples = []

        for batch in data:
            fourierSample = list(Fourier.get_amplitudes_and_phases(batch))
            Plotter.draw(fourierSample, color = ['green', 'midnightblue', 'red'], file_path = 'Maths/plot/fig.png',
                         x_label="frequency", y_label="amplitude", name="Frequency response")

            sample_ok : bool = self.__recordingPresenter__.processSampleDialog('Maths/plot/fig.png')
            if sample_ok:
                samples.append(Sample(signals = fourierSample,
                                    angle = self.__params__.angle,
                                    bad_data = False,
                                    frequency = self.__params__.frequency,
                                    person = self.__params__.person))

        Dataset(file_path=self.__params__.filename).addData(arr = samples, sync = True)
