from dataclasses import dataclass
from PyQt6 import QtWidgets, uic
import sys
import serial.tools.list_ports

from Arduino import ArduinoController

@dataclass(frozen=True)
class UserDefinedParameters:
    port: str
    filename: str
    person: str

    frequency: int
    batchSize: int
    angle: int


class SettingsPresenter:
    def setSettingsWindowsView(self, settingsWindowView):
        self.__settingsWindowView__ = settingsWindowView

    def setSettingsModel(self, settingsModel):
        self.__settingsModel__ = settingsModel

    def startReadingSignal(self):
        self.__settingsWindowView__.applyButton.setEnabled(False)
        self.__settingsModel__.readSamples(self.__settingsWindowView__.getUserDefinedParameters())

    def finishedReadingSignal(self):
        self.__settingsWindowView__.applyButton.setEnabled(True)
        self.__settingsWindowView__.showBadDataDialog()



class SettingsWindowView(QtWidgets.QMainWindow):
    __settingsPresenter__ : SettingsPresenter

    def __init_widgets__(self):
        self.filenameLineEdit = self.findChild(QtWidgets.QLineEdit, 'filenameLineEdit')
        self.personLineEdit = self.findChild(QtWidgets.QLineEdit, 'personLineEdit')

        self.frequencySpinBox = self.findChild(QtWidgets.QSpinBox, 'frequencySpinBox')
        self.batchSizeSpinBox = self.findChild(QtWidgets.QSpinBox, 'batchSizeSpinBox')
        self.angleSpinBox = self.findChild(QtWidgets.QSpinBox, 'angleSpinBox')

        self.portComboBox = self.findChild(QtWidgets.QComboBox, 'portComboBox')

        self.refreshButton = self.findChild(QtWidgets.QPushButton, 'refreshButton')
        self.refreshButton.clicked.connect(self.__refreshPorts__) 

        self.applyButton = self.findChild(QtWidgets.QPushButton, 'applyButton')
        self.applyButton.clicked.connect(self.__applyButtonPressed__) 

    def __init__(self, settingsPresenter : SettingsPresenter):
        super(SettingsWindowView, self).__init__()
        uic.loadUi('ui/settingsWindow.ui', self)

        self.__init_widgets__()
        self.__refreshPorts__()
        self.__settingsPresenter__ = settingsPresenter

        self.show()

    def __refreshPorts__(self):
        self.portComboBox.clear()
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            self.portComboBox.addItem(p.device)


    def __applyButtonPressed__(self):
        self.__settingsPresenter__.startReadingSignal()

    def showBadDataDialog(self):
        print('a')

    def getUserDefinedParameters(self) -> UserDefinedParameters:
        port = self.portLineEdit.text()
        filename = self.filenameLineEdit.text()
        person = self.personLineEdit.text()

        frequency = self.frequencySpinBox.value()
        batchSize = self.batchSizeSpinBox.value()
        angle = self.angleSpinBox.value()

        return UserDefinedParameters(port, filename, person, frequency, batchSize, angle)




class SettingsModel:
    def __init__(self, settingsPresenter : SettingsPresenter):
        self.__settingsPresenter__ = settingsPresenter

    def readSamples(self, userDefinedParameters : UserDefinedParameters):
        params = userDefinedParameters
        print(params)

        # arduinoController = ArduinoController(batch_size = params.batchSize, port = params.port)
        # arduinoController.recordData()

        self.__settingsPresenter__.finishedReadingSignal()



def main():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print(p.device)

    app = QtWidgets.QApplication(sys.argv)

    presenter = SettingsPresenter()
    window = SettingsWindowView(presenter)
    model = SettingsModel(presenter)

    presenter.setSettingsModel(model)
    presenter.setSettingsWindowsView(window)

    app.exec()

if __name__ == '__main__':
    main()