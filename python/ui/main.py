import asyncio
from PyQt6 import QtCore, QtWidgets, uic
import sys

from python.ui.QuestionDialogView import QuestionDialogView
from python.ui.RecordingModel import RecordingModel
from python.ui.RecordingPresenter import RecordingPresenter
from python.ui.SettingsWindowView import SettingsWindowView


def main():
    app = QtWidgets.QApplication(sys.argv)

    presenter = RecordingPresenter()
    window = SettingsWindowView(presenter)
    model = RecordingModel(presenter)
    dialog = QuestionDialogView()

    presenter.setSettingsModel(model)
    presenter.setSettingsWindowView(window)
    presenter.setFineDialogView(dialog)

    asyncio.run(app.exec())


if __name__ == '__main__':
    main()