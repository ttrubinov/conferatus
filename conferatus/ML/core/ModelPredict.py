import json
import os

import numpy as np
from keras import Sequential
from tensorflow import keras
import tensorflow as tf


class ModelPredict:

    @staticmethod
    def download(dir_path="./model_dir", prefix=None):
        if prefix is None:
            prefix = ""
        else:
            prefix += "_"
        filepath = dir_path + "/" + prefix
        model_angle = keras.models.load_model(filepath + "model_angle")
        model_freq = keras.models.load_model(filepath + "model_freq")
        model_classification = keras.models.load_model(filepath + "model_classification")
        model_person = keras.models.load_model(filepath + "model_person")
        conf: dict
        with open(filepath + "model_conf.json", mode="r", encoding='utf-8') as confFile:
            conf = json.load(confFile)

        return ModelPredict(model_classification=model_classification, model_angle=model_angle,
                            model_freq=model_freq, model_person=model_person, **conf)

    def __init__(self, model_classification: Sequential, model_angle: Sequential, model_freq: Sequential,
                 model_person: Sequential, num_to_person_dict: dict, max_freq: float,
                 max_angle: float):
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
        max_arg: int = np.argmax(pred)
        print(pred, max_arg)
        return self.cls[max_arg], pred[max_arg]

    # TODO: add more predictions,

    def save(self, dir_path="./model_dir", prefix=None):
        if prefix is None:
            prefix = ""
        else:
            prefix += "_"
        if dir_path[-1] != "/":
            dir_path = dir_path + "/"
        os.makedirs(dir_path, exist_ok=True)
        self.model_angle.save(dir_path + prefix + "model_angle")
        self.model_classification.save(dir_path + prefix + "model_classification")
        self.model_freq.save(dir_path + prefix + "model_freq")
        self.model_person.save(dir_path + prefix + "model_person")
        conf = {
            "num_to_person_dict": self.num_to_person_dict,
            "max_freq": self.max_freq,
            "max_angle": self.max_angle
        }

        with open(dir_path + prefix + "model_conf.json", mode="w", encoding='utf-8') as confFile:
            print(json.dumps(conf), file=confFile)