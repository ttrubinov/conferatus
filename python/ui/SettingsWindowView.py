from PyQt6 import QtWidgets, uic

from python.ui.RecordingPresenter import RecordingPresenter
import serial.tools.list_ports

from python.ui.UserDefinedParamerers import UserDefinedParameters

class SettingsWindowView(QtWidgets.QMainWindow):
    def __init_widgets__(self):
        self.filenameLineEdit = self.findChild(QtWidgets.QLineEdit, 'filenameLineEdit')
        self.personLineEdit = self.findChild(QtWidgets.QLineEdit, 'personLineEdit')
        self.frequencySpinBox = self.findChild(QtWidgets.QSpinBox, 'frequencySpinBox')
        self.batchSizeSpinBox = self.findChild(QtWidgets.QSpinBox, 'batchSizeSpinBox')
        self.angleSpinBox = self.findChild(QtWidgets.QSpinBox, 'angleSpinBox')
        self.portComboBox = self.findChild(QtWidgets.QComboBox, 'portComboBox')
        self.refreshButton = self.findChild(QtWidgets.QPushButton, 'refreshButton')
        self.applyButton = self.findChild(QtWidgets.QPushButton, 'applyButton')
        self.statusbar = self.findChild(QtWidgets.QStatusBar, 'statusbar')

    def __init__(self, recordingPresenter : RecordingPresenter):
        super(SettingsWindowView, self).__init__()
        uic.loadUi('ui/settingsWindow.ui', self)
        self.__recordingPresenter__ = recordingPresenter

        self.__init_widgets__()
        self.__refreshPorts__()

        self.refreshButton.clicked.connect(self.__refreshPorts__) 
        self.applyButton.clicked.connect(self.__applyButtonPressed__) 
        self.statusbar.showMessage("Inactive")

        self.show()

    def __refreshPorts__(self):
        self.portComboBox.clear()
        portList = list(serial.tools.list_ports.comports())

        if portList:
            self.applyButton.setEnabled(True)
            for port in portList:
                self.portComboBox.addItem(port.device)
        else:
            self.applyButton.setEnabled(False)
        

    def __applyButtonPressed__(self):
        self.__refreshPorts__()
        self.__recordingPresenter__.startReadingSamples()


    def getUserDefinedParameters(self) -> UserDefinedParameters:
        port = self.portComboBox.currentText()
        filename = self.filenameLineEdit.text()
        person = self.personLineEdit.text()

        frequency = self.frequencySpinBox.value()
        batchSize = self.batchSizeSpinBox.value()
        angle = self.angleSpinBox.value()

        return UserDefinedParameters(port, filename, person, frequency, batchSize, angle)