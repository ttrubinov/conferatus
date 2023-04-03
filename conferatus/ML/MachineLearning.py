import numpy as np
# from keras import Sequential
# from keras.layers import Dense
from sklearn.model_selection import train_test_split
from tensorflow import keras
import tensorflow as tf

from conferatus.ML.Datasets.Dataset import Sample


class BasicModel:

    @staticmethod
    def _base_layer(data_amount=250, mic_amount=3):
        mic_inputs = keras.layers.Input(shape=(mic_amount, data_amount))
        dense = keras.layers.Dense(64, activation="relu")(mic_inputs)
        x = keras.layers.Dense(64, activation="relu")(dense)
        return mic_inputs, x

    def __init__(self, sample_size=250, mic_amount=3, person_dict: dict = None, max_frequency=1000,
                 max_angle=180):
        if not (person_dict is None):
            self.person_dict = person_dict
            self.person_dict[""] = 0
        else:
            self.person_dict = {"": 0, "Misha": 1, "Pasha": 2, "Tima": 3}
        self.maxFrequency = max_frequency
        self.max_angle = max_angle

        inp, model_classification_layer = \
            BasicModel._base_layer(data_amount=sample_size, mic_amount=mic_amount)
        model_classification_layer = keras.layers.Dense(3)(model_classification_layer)
        self.model_classification = tf.keras.Model(inputs=inp, outputs=model_classification_layer)
        self.model_classification.compile(optimizer='adam',
                                          loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True))

        # model_angle_layer = BasicModel._base_layer(data_amount=sample_size, mic_amount=mic_amount)
        # model_angle_layer = keras.layers.Dense(1)(model_angle_layer)
        # self.model_angle = tf.keras.Sequential([model_angle_layer])
        # self.model_angle.compile(optimizer='adam',
        #                          loss=keras.losses.mse)
        #
        # model_freq_layer = BasicModel._base_layer(data_amount=sample_size, mic_amount=mic_amount)
        # model_freq_layer = keras.layers.Dense(1)(model_freq_layer)
        # self.model_freq = tf.keras.Sequential([model_freq_layer])
        # self.model_freq.compile(optimizer='adam',
        #                         loss=keras.losses.mse)
        #
        # model_person_layer = BasicModel._base_layer(data_amount=sample_size, mic_amount=mic_amount)
        # model_person_layer = keras.layers.Dense(len(person_dict))(model_person_layer)
        # self.model_person = tf.keras.Sequential([model_person_layer])
        # self.model_person.compile(optimizer='adam',
        #                           loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True))

    @staticmethod
    def prepare_data(data: list[Sample], person_dict: dict, max_freq: int, max_angle: int):
        classification_data = ([], [])
        angle_data = ([], [])
        freq_data = ([], [])
        person_data = ([], [])
        for sample in data:
            signals = sample.signals
            classification_data[0].append(signals)
            if sample.bad_data:
                classification_data[1].append(0)
            elif sample.frequency is not None:
                freq_data[0].append(signals)
                freq_data[1].append(sample.frequency / max_freq)
                classification_data[1].append(1)
            elif sample.person is not None:
                person_data[0].append(signals)
                if sample.person in person_dict:
                    person_data[1].append(person_dict[sample.person])
                else:
                    person_data[1].append(0)
                classification_data[1].append(2)
            else:
                raise sample
            if not sample.bad_data:
                angle_data[0].append(signals)
                angle_data[1].append(sample.angle / max_angle)

        return {
            "classification_data": classification_data,
            "angle_data": angle_data,
            "freq_data": freq_data,
            "person_data": person_data
        }

    def fit(self, data: list[Sample], epochs=500):
        prepared = BasicModel.prepare_data(data, self.person_dict, self.maxFrequency, self.max_angle)
        classification_data = prepared["classification_data"]
        angle_data = prepared["angle_data"]
        freq_data = prepared["freq_data"]
        person_data = prepared["person_data"]
        self.model_classification.fit(classification_data[0], classification_data[1], epochs=epochs)
        pass

    def predict_class(self, data: list[list[float]]):
        return self.model_classification.predict(data)


if __name__ == '__main__':
    model = BasicModel(sample_size=1, mic_amount=1)
    model.fit([Sample([[1]], 90, frequency=500), Sample([[0]], bad_data=True)])
    print(model.predict_class([[1]]))
    print(model.predict_class([[0]]))
    pass
