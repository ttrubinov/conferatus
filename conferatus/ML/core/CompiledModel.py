import numpy as np
from keras import Sequential
from tensorflow import keras
import tensorflow as tf


class CompiledModel:

    @staticmethod
    def download(filepath: str):
        # TODO: loading from json parameters, load models
        return keras.models.load_model(filepath)

    def __init__(self, model_classification: Sequential, model_angle: Sequential, model_freq: Sequential,
                 model_person: Sequential, num_to_person_dict: dict, max_freq,
                 max_angle):
        self.max_angle = max_angle
        self.max_freq = max_freq
        self.num_to_person_dict = num_to_person_dict
        self.model_person = model_person
        self.model_freq = model_freq
        self.model_angle = model_angle
        self.model_classification = model_classification
        self.cls = {0: "bad_data", 1: "frequency", 2: "person"}

    def predict_class(self, data: list[list[list[float]]]):
        pred = self.model_classification.predict(data)[0][0]
        print(pred)
        max_arg : int = np.argmax(pred)
        print(pred, max_arg)
        return self.cls[max_arg], pred[max_arg]

    # TODO: add more predictions,


    def save(self, file_path):
        #TODO: saving into json parameters, saving models
        pass
