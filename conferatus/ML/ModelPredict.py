class ModelPredict:
    def __init__(self, model_file_path: str) -> None:
        self.model = model_file_path.open()

    def get_predict(self, data: list[list[float]]) -> bool:
        if self.model.predict(data) == "badData":
            return False
        else:
            return True

    def get_angle(self, data: list[list[float]]) -> int:
        return self.model.get_angle(data)

    def get_person(self, data: list[list[float]]) -> str:
        return self.model.get_person(data)
