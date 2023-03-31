import json
import pathlib


class Sample:
    def __init__(self, signals: list[list[float]], angle: float, bad_data=False, frequency=None, person: str = None):
        self.angle = angle
        self.signals = signals
        self.frequency = frequency
        self.bad_data = bad_data
        self.person = person

    def __repr__(self):
        return f"Sample angle:{self.angle}, freq:{self.frequency}, bad_data:{self.bad_data}, " \
               f"person:{self.person}, signals:{self.signals}"


class Dataset:
    def __init__(self, filePath="conferatus.json"):
        self.filePath = filePath
        self.currentData = []
        if not pathlib.Path(filePath).is_file():
            with open(filePath, "w", encoding='utf-8') as fileData:
                print(json.dumps(list()), file=fileData)
        else:
            with open(self.filePath, "r", encoding='utf-8') as fileData:
                self.currentData = [Sample(signals=data['signals'],
                                           angle=data['angle'],
                                           bad_data=data['bad_data'],
                                           frequency=data['frequency'],
                                           person=data['person']) for data in
                                    json.load(fileData)]

    def getSampleData(self):
        return self.currentData

    def saveData(self, arr: list[Sample], file_path=None):
        if file_path is None:
            file_path = self.filePath
        with open(file_path, "w", encoding='utf-8') as fileData:
            if arr is not None:
                print(json.dumps([i.__dict__ for i in arr]), file=fileData)

    def addData(self, arr: list[Sample], file_path=None):
        if file_path is None:
            file_path = self.filePath
        self.currentData += arr
        with open(file_path, "w", encoding='utf-8') as fileData:
            print(json.dumps([i.__dict__ for i in self.currentData]), file=fileData)


if __name__ == '__main__':
    dt = Dataset()
    dt.saveData([Sample(signals=[[1], [1], [1]], angle=0, frequency=500, person=None)])
    print(dt.getSampleData())
