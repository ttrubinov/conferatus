from PyQt6 import QtGui, QtWidgets, uic

class QuestionDialogView(QtWidgets.QDialog):
    def __init__(self):
        super(QuestionDialogView, self).__init__()
        uic.loadUi('ui/recordingsOkDialog.ui', self)

        self.__plotterImage = self.findChild(QtWidgets.QLabel, 'plotterLabel')

    def setPicture(self, imagePath):
        pixmap = QtGui.QPixmap()
        pixmap.load(imagePath)

        self.__plotterImage.setPixmap(pixmap)

