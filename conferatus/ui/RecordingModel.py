from raytracing.Fourier import Fourier
from raytracing.Dataset import Dataset, Sample
from raytracing.Plotter import Plotter
from raytracing.ArduinoController import ArduinoController

from ui.RecordingPresenter import RecordingPresenter
from ui.UserDefinedParamerers import UserDefinedParameters
from PyQt6 import QtCore, QtWidgets

class RecordingThread(QtCore.QThread):
    def __init__(self, recordingPresenter, params : UserDefinedParameters, parent=None):
        super(RecordingThread, self).__init__(parent)
        self.__recordingPresenter__ = recordingPresenter
        self.__params__ = params
        
    def run(self):
        with ArduinoController(batch_size = self.__params__.batchSize, port = self.__params__.port) as arduinoController:
            data = arduinoController.recordData()

        for i in range(0, self.__params__.batchSize):
            fourierSample = Fourier.get_amplitudes_and_phases(data[i])
            # Plotter.draw(fourierSample)

            # Plottr().show()
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
