import json
import pathlib

from conferatus.Maths.Fourier import Fourier
from conferatus.Maths.Plotter import Plotter


class Sample:
    def __init__(self, signals: list[list[float]], angle: float = None, bad_data=False, frequency=None,
                 person: str = None):
        self.angle = angle
        self.signals = signals
        self.frequency = frequency
        self.bad_data = bad_data
        self.person = person

    def __repr__(self):
        return f"Sample angle:{self.angle}, freq:{self.frequency}, bad_data:{self.bad_data}, " \
               f"person:{self.person}, signals:{len(self.signals), len(self.signals[0])}"


class Dataset:
    def __init__(self, file_path="conferatus.json"):
        """
        Creating or open the file with samples and loads
        :param file_path: the path of the file
        """
        self.file_path = file_path
        self.currentData = []
        if not pathlib.Path(file_path).is_file():
            with open(file_path, "w", encoding='utf-8') as fileData:
                print(json.dumps(list()), file=fileData)
        else:
            with open(self.file_path, "r", encoding='utf-8') as fileData:
                self.currentData = [Sample(signals=data['signals'],
                                           angle=data['angle'],
                                           bad_data=data['bad_data'],
                                           frequency=data['frequency'],
                                           person=data['person']) for data in
                                    json.load(fileData)]

    def getSampleData(self, sync=False, file_path: str = None):
        """
        :param file_path: the file_path for getting data
        :param sync: flag for getting from the file and sync
        :return: the list of samples
        """
        if file_path is None:
            file_path = self.file_path
        if sync:
            with open(file_path, "r", encoding='utf-8') as fileData:
                self.currentData = [Sample(**data) for data in
                                    json.load(fileData)]
        return self.currentData

    @staticmethod
    def get_samples(file_path: str = None):
        with open(file_path, "r", encoding='utf-8') as fileData:
            return [Sample(**data) for data in
                    json.load(fileData)]

    def saveData(self, arr: list[Sample] = None, sync=False, file_path=None):
        """
        Saving data into the file, into the memory.

        :param arr: list of samples for saving (None for saving current Data)
        :param sync: flag to save into the file
        :param file_path: path of the file
        :return: nothing
        """
        if file_path is None:
            file_path = self.file_path
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
            file_path = self.file_path
        self.currentData += arr
        if sync:
            with open(file_path, "w", encoding='utf-8') as fileData:
                print(json.dumps([i.__dict__ for i in self.currentData]), file=fileData)
        return self.currentData


if __name__ == '__main__':
    ampl, phases = Fourier.get_amplitudes_and_phases(Dataset.get_samples("2128_2_real.json").pop(2).signals,
                                                     should_calculate_phases=True)
    Plotter.draw(ampl, color=["r", "g", "b"], file_path="hui1.png", x_label="frequency",
                 y_label="amplitude", name="Amplitude response", legend=["left Mic", "middle Mic", "right Mic"])
    Plotter.draw(phases, color=["r", "g", "b"], file_path="hui2.png",
                 x_label="frequency", y_label="phase", name="Phases response",
                 legend=["left Mic", "middle Mic", "right Mic"])
    print()
