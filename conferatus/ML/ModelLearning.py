import abc

from conferatus.conferatus.ML.Datasets.Dataset import Dataset


class ModelLearning:
    def __init__(self, mode_file_path: str) -> None:
        self.model = mode_file_path.aboba()

    def train_model(data: Dataset):
        pass
