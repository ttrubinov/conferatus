from PyQt6 import QtCore, QtWidgets, uic
import sys

from ui.QuestionDialogView import QuestionDialogView
from ui.RecordingModel import RecordingModel
from ui.RecordingPresenter import RecordingPresenter
from ui.SettingsWindowView import SettingsWindowView


def main():
    app = QtWidgets.QApplication(sys.argv)

    presenter = RecordingPresenter()
    window = SettingsWindowView(presenter)
    model = RecordingModel(presenter)
    dialog = QuestionDialogView()

    presenter.setSettingsModel(model)
    presenter.setSettingsWindowView(window)
    presenter.setFineDialogView(dialog)

    app.exec()


if __name__ == '__main__':
    main()