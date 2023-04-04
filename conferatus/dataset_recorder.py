#!/usr/bin/python3

from PyQt6 import QtWidgets
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

    # T = 1 / 12000
    # data = [[], [], []]
    # with open("oldExamples/samples/waiting505.txt", mode="r") as f:
    #     s = f.readline()
    #     nn = 250
    #     counter = 0
    #     while True:
    #         s = f.readline()
    #         if "End" in s:
    #             break
    #         if counter % nn == 0:
    #             for i in data:
    #                 i.append([])
    #         s = s.split()
    #         for i in range(0, 3):
    #             data[i][counter // nn].append(float(s[i]))
    #         counter += 1
    #
    # fourierSample = Fourier.get_amplitudes_and_phases([data[0][0], data[1][0], data[2][0]])
    # Plotter.draw(fourierSample, color=["red", "blue", "green"])


