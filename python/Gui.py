from PyQt6 import QtWidgets, uic
import sys

from Arduino import ArduinoController

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('ui/settingsWindow.ui', self)

        self.portLineEdit = self.findChild(QtWidgets.QLineEdit, 'portLineEdit')
        self.frequencySpinBox = self.findChild(QtWidgets.QSpinBox, 'frequencySpinBox')

        self.batchSizeSpinBox = self.findChild(QtWidgets.QSpinBox, 'batchSizeSpinBox')

        self.applyButton = self.findChild(QtWidgets.QPushButton, 'applyButton') # Find the button
        self.applyButton.clicked.connect(self.applyButtonPressed) 

        self.show()

    def applyButtonPressed(self):
        port = self.portLineEdit.text()
        frequency = self.frequencySpinBox.value()
        batchSize = self.batchSizeSpinBox.value()

        print(port)
        print(frequency)
        print(batchSize)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec()

    with ArduinoController(3, 230400, 1) as controller:
        samples = controller.recordSamples()

if __name__ == '__main__':
    main()