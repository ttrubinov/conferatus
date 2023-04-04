class RecordingPresenter:
    def setSettingsWindowView(self, settingsWindowView):
        self.__settingsWindowView__ = settingsWindowView

    def setSettingsModel(self, settingsModel):
        self.__settingsModel__ = settingsModel

    def setFineDialogView(self, fineDialogView):
        self.__fineDialogView__ = fineDialogView

    def startReadingSamples(self):
        self.__settingsWindowView__.applyButton.setEnabled(False)
        self.__settingsWindowView__.statusbar.showMessage("Recording...")
        self.__settingsModel__.readSamples(self.__settingsWindowView__.getUserDefinedParameters())

    def processSampleDialog(self, imagePath) -> bool:
        self.__fineDialogView__.setPicture(imagePath)
        return self.__fineDialogView__.exec()
    
    def finishedReadingSamples(self):
        self.__settingsWindowView__.applyButton.setEnabled(True)
        self.__settingsWindowView__.statusbar.showMessage("Inactive")

