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
        """
        Creating or open the file with samples and loads
        :param filePath: the path of the file
        """
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

    def getSampleData(self, sync=False):
        """

        :param sync: flag for getting from the file and sync
        :return: the list of samples
        """
        if sync:
            with open(self.filePath, "r", encoding='utf-8') as fileData:
                self.currentData = [Sample(signals=data['signals'],
                                           angle=data['angle'],
                                           bad_data=data['bad_data'],
                                           frequency=data['frequency'],
                                           person=data['person']) for data in
                                    json.load(fileData)]
        return self.currentData

    def saveData(self, arr: list[Sample] = None, sync=False, file_path=None):
        """
        Saving data into the file, into the memory.

        :param arr: list of samples for saving (None for saving current Data)
        :param sync: flag to save into the file
        :param file_path: path of the file
        :return: nothing
        """
        if file_path is None:
            file_path = self.filePath
        self.currentData = arr
        if sync:
            with open(file_path, "w", encoding='utf-8') as fileData:
                if arr is not None:
                    print(json.dumps([i.__dict__ for i in arr]), file=fileData)
                else:
                    print(json.dumps([i.__dict__ for i in self.currentData]), file=fileData)
        else:
            if arr is None:
                with open(file_path, "w", encoding='utf-8') as fileData:
                    print(json.dumps([i.__dict__ for i in self.currentData]), file=fileData)

    def addData(self, arr: list[Sample], sync=False, file_path=None):
        """
        Adding new samples
        :param arr: data for adding
        :param sync: flag for saving into the file
        :param file_path: path of the file
        :return: currentData
        """
        if file_path is None:
            file_path = self.filePath
        self.currentData += arr
        if sync:
            with open(file_path, "w", encoding='utf-8') as fileData:
                print(json.dumps([i.__dict__ for i in self.currentData]), file=fileData)
        return self.currentData


if __name__ == '__main__':
    dt = Dataset()
    dt.saveData(arr=[Sample(signals=[[1], [1], [1]], angle=0, bad_data=False, frequency=500, person=None)],
                sync=True)
    print(dt.getSampleData())
