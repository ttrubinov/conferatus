import json
import pathlib


class Sample:
    def __init__(self, signals: list[list[float]], angle: float, frequency=None, person: str = None):
        self.angle = angle
        self.signals = signals
        self.frequency = frequency
        self.person = person

    def __repr__(self):
        print(self.angle)
        return f"Sample angle:{self.angle}, freq:{self.frequency}, person:{self.person}, signals:{self.signals}"


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

    def getSampleData(self):
        data = self.getFileData()
        return [Sample(samp['angle'], samp['signals'], samp['frequency'], samp['person']) for samp in data]

    def saveData(self, arr: list[Sample]):
        with open(self.filePath, "w", encoding='utf-8') as fileData:
            print(json.dumps([i.__dict__ for i in arr]), file=fileData)


if __name__ == '__main__':
    dt = Dataset()
    dt.saveData([Sample(signals=[[1], [1], [1]], angle=0, frequency=500, person=None)])
    print(dt.getSampleData())
