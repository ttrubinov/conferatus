from Maths.Fourier import Fourier
from ML.Datasets.Dataset import Dataset, Sample
from Maths.Plotter import Plotter
from Arduino.ArduinoController import ArduinoController

from ui.RecordingPresenter import RecordingPresenter
from ui.UserDefinedParamerers import UserDefinedParameters
from PyQt6 import QtCore


class RecordingThread(QtCore.QThread):
    def __init__(self, params : UserDefinedParameters, parent=None):
        super(RecordingThread, self).__init__(parent)
        self.__params = params

    def run(self):
        with ArduinoController(batch_size = self.__params.batchSize, port = self.__params.port) as arduinoController:
            self.__data = arduinoController.recordData()

    def data(self):
        return self.__data
    
    def params(self):
        return self.__params


class RecordingModel:
    def __init__(self, recordingPresenter : RecordingPresenter):
        self.__recordingPresenter = recordingPresenter

    def readSamples(self, params : UserDefinedParameters):
        print(params)

        self.__thread = RecordingThread(params)
        self.__thread.finished.connect(self.__finishedReadingSamples)
        self.__thread.start()

    def __finishedReadingSamples(self):
        self.selectSamples(self.__thread.data(), self.__thread.params())
        self.__recordingPresenter.finishedReadingSamples()

    def selectSamples(self, data, params : UserDefinedParameters):
        samples = []
        real = []

        for batch in data:
            fourierSample = list(Fourier.get_amplitudes_and_phases(batch))
            Plotter.draw(fourierSample, color = ['green', 'midnightblue', 'red'], file_path = 'Maths/plot/fig.png',
                         x_label="frequency", y_label="amplitude", name="Frequency response")

            sample_ok : bool = self.__recordingPresenter.processSampleDialog('Maths/plot/fig.png')
            if sample_ok:
                real.append(Sample(signals = batch,
                                    angle = params.angle,
                                    bad_data = False,
                                    frequency = params.frequency,
                                    person = params.person))
                samples.append(Sample(signals = fourierSample,
                                    angle = params.angle,
                                    bad_data = False,
                                    frequency = params.frequency,
                                    person = params.person))

        Dataset(file_path=params.filename + ".json").addData(arr = samples, sync = True)
        Dataset(file_path=params.filename + "_real.json").addData(arr = real, sync = True)
