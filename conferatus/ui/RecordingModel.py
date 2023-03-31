

from raytracing.Arduino import ArduinoController
from ui.RecordingPresenter import RecordingPresenter
from ui.UserDefinedParamerers import UserDefinedParameters
from PyQt6 import QtCore


class RecordingThread(QtCore.QThread):
    def __init__(self, settingsPresenter, params : UserDefinedParameters, parent=None):
        super(RecordingThread, self).__init__(parent)
        self.__settingsPresenter__ = settingsPresenter
        self.__params__ = params
        
    def run(self):
        with ArduinoController(batch_size = self.__params__.batchSize, port = self.__params__.port) as arduinoController:
            data = arduinoController.recordData()

        for i in range(0, self.__params__.batchSize):
            # open plotter
            print(self.__settingsPresenter__.processSampleDialog())


class RecordingModel:
    def __init__(self, settingsPresenter : RecordingPresenter):
        self.__settingsPresenter__ = settingsPresenter

    def readSamples(self, params : UserDefinedParameters):
        print(params)

        self.thread = RecordingThread(self.__settingsPresenter__, params)
        self.thread.finished.connect(self.__settingsPresenter__.finishedReadingSamples)

        self.thread.start()
