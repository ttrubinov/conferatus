from PyQt6 import QtWidgets, uic

class QuestionDialogView(QtWidgets.QDialog):
    def __init__(self):
        super(QuestionDialogView, self).__init__()
        uic.loadUi('ui/recordingsOkDialog.ui', self)