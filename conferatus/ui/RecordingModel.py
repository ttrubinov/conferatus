

from raytracing.Arduino import ArduinoController
from ui.RecordingPresenter import RecordingPresenter
from ui.UserDefinedParamerers import UserDefinedParameters


class RecordingModel:
    def __init__(self, settingsPresenter : RecordingPresenter):
        self.__settingsPresenter__ = settingsPresenter

    def readSamples(self, userDefinedParameters : UserDefinedParameters):
        params = userDefinedParameters
        print(params)

        with ArduinoController(batch_size = params.batchSize, port = params.port) as arduinoController:
            data = arduinoController.recordData()
            # todo qthread


        for i in range(0, params.batchSize):
            # open plotter
            print(self.__settingsPresenter__.processSampleDialog())

        

        self.__settingsPresenter__.finishedReadingSamples()