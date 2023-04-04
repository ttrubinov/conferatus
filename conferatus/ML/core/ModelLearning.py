import itertools

import numpy as np
from tensorflow import keras
import tensorflow as tf

from conferatus.ML.Datasets.Dataset import Sample
from conferatus.ML.core.ModelPredict import ModelPredict


class ModelLearning:

    @staticmethod
    def _base_layer(data_amount=250, mic_amount=3):
        mic_inputs = keras.layers.Input(shape=(mic_amount * data_amount))
        dense = keras.layers.Dense(64, activation="relu")(mic_inputs)
        x = keras.layers.Dense(64, activation="relu")(dense)
        return mic_inputs, x

    def __init__(self, sample_size=250, mic_amount=3, person_dict: dict = None, max_frequency=1000,
                 max_angle=180):
        if not (person_dict is None):
            self.person_dict = person_dict
            self.person_dict[""] = 0
        else:
            self.person_dict = {"": 0, "Pasha": 1, "Misha": 2, "Tima": 3}
        self.maxFrequency = max_frequency
        self.max_angle = max_angle

        inp, model_classification_layer = \
            ModelLearning._base_layer(data_amount=sample_size, mic_amount=mic_amount)
        model_classification_layer = keras.layers.Dense(3)(model_classification_layer)
        self.model_classification = tf.keras.Model(inputs=inp, outputs=model_classification_layer)
        self.model_classification.compile(optimizer='adam',
                                          loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True))

        inp, model_angle_layer = ModelLearning._base_layer(data_amount=sample_size, mic_amount=mic_amount)
        model_angle_layer = keras.layers.Dense(1)(model_angle_layer)
        self.model_angle = tf.keras.Model(inputs=inp, outputs=model_angle_layer)
        self.model_angle.compile(optimizer='adam',
                                 loss=keras.losses.mse)

        inp, model_freq_layer = ModelLearning._base_layer(data_amount=sample_size, mic_amount=mic_amount)
        model_freq_layer = keras.layers.Dense(1)(model_freq_layer)
        self.model_freq = tf.keras.Model(inputs=inp, outputs=model_freq_layer)
        self.model_freq.compile(optimizer='adam',
                                loss=keras.losses.mse)

        inp, model_person_layer = ModelLearning._base_layer(data_amount=sample_size, mic_amount=mic_amount)
        model_person_layer = keras.layers.Dense(4)(model_person_layer) #
        self.model_person = tf.keras.Model(inputs=inp, outputs=model_person_layer)
        self.model_person.compile(optimizer='adam',
                                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True))

    @staticmethod
    def prepare_data(data: list[Sample], person_dict: dict, max_freq: int, max_angle: int):
        classification_data = ([], [])
        angle_data = ([], [])
        freq_data = ([], [])
        person_data = ([], [])
        for sample in data:
            signals = list(itertools.chain.from_iterable(sample.signals))
            classification_data[0].append(signals)
            if sample.bad_data:
                classification_data[1].append(0)
            elif not (sample.frequency is None):
                freq_data[0].append(signals)
                freq_data[1].append(sample.frequency / max_freq)
                classification_data[1].append(1)
            elif not (sample.person is None):
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
        print(person_data)
        return {
            "classification_data": classification_data,
            "angle_data": angle_data,
            "freq_data": freq_data,
            "person_data": person_data
        }

    def fit(self, data: list[Sample], epochs=500):
        prepared = ModelLearning.prepare_data(data, self.person_dict, self.maxFrequency, self.max_angle)
        classification_data = prepared["classification_data"]
        angle_data = prepared["angle_data"]
        freq_data = prepared["freq_data"]
        person_data = prepared["person_data"]
        self.model_classification.fit(classification_data[0], classification_data[1], epochs=epochs)
        self.model_angle.fit(angle_data[0], angle_data[1], epochs=epochs)
        self.model_freq.fit(freq_data[0], freq_data[1], epochs=epochs)
        self.model_person.fit(person_data[0], person_data[1], epochs=epochs)

    def compile(self) -> ModelPredict:
        self.model_classification = tf.keras.Sequential([self.model_classification,
                                                         tf.keras.layers.Softmax()])
        self.model_person = tf.keras.Sequential([self.model_person,
                                                 tf.keras.layers.Softmax()])
        return ModelPredict(model_classification=self.model_classification, model_angle=self.model_angle,
                            model_freq=self.model_freq, model_person=self.model_person,
                            num_to_person_dict={int(v): k for k, v in self.person_dict.items()},
                            max_freq=self.maxFrequency,
                            max_angle=self.max_angle)


if __name__ == '__main__':
    model = ModelLearning(sample_size=2, mic_amount=2)
    model.fit([Sample([[0.7, 0.6], [0.6, 0.7]], 90, person="Misha"), Sample([[0.3, 0.4], [0.4, 0.3]], 90, frequency=500),
               Sample([[0, 0.1], [0.1, 0]], bad_data=True), Sample([[0.9, 0.9], [0.9, 0.9]], 90, person="Misha")],
              epochs=250)
    comp_model = model.compile()
    comp_model.save()
    another = ModelPredict.download()
    # another = model.compile()
    print(another.predict_all([[0, 0], [0, 0]]))
    print(another.predict_all([[0.3, 0.4], [0.4, 0.3]]))
    print(another.predict_all([[0.7, 0.6], [0.6, 0.7]]))
    print(another.predict_all([[0.9, 0.9], [0.9, 0.9]]))

    pass
