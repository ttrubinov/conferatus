import json
import pathlib
from types import SimpleNamespace


class Sample:
    def __init__(self, signals: list[list[float]], angle: float):
        self.angle = angle
        self.signals = signals
        pass


class Dataset:
    def __init__(self, filePath="conferatus.json"):
        self.filePath = filePath
        self.currentData = None
        if not pathlib.Path(filePath).is_file():
            with open(filePath, "w", encoding='utf-8') as fileData:
                print(json.dumps(list()), file=fileData)

    def getFileData(self):
        with open(self.filePath, "r", encoding='utf-8') as fileData:
            self.currentData = json.load(fileData)
        return self.currentData

    def saveData(self, arr: list[Sample]):
        with open(self.filePath, "w", encoding='utf-8') as fileData:
            print(json.dumps([i.__dict__ for i in arr]), file=fileData)
