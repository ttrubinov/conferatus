import itertools
import random

from conferatus.ML.Datasets.Dataset import Sample, Dataset
from conferatus.ML.core.ModelLearning import ModelLearning
from conferatus.ML.core.ModelPredict import ModelPredict
from conferatus.Maths.Plotter import Plotter


def get_samples_from_resources(file_paths: list, max_data=None) -> list[Sample]:
    arr: list[list[Sample]] = []
    for file_path in file_paths:
        samples: list[Sample] = Dataset.get_samples(file_path)
        for i in range(len(samples)):
            for j in range(0, len(samples[i].signals)):
                samples[i].signals[j] = samples[i].signals[j][:max_data]
        arr.append(samples)
    return list(itertools.chain.from_iterable(arr))


def main():
    file_paths = [  # "freqDataSet.json",
        "freakNewDataSet.json",
        "freakThirdDataSet.json", "BreakingBadData.json"]
    mic_amount = 3
    sample_size = 100
    model = ModelLearning(sample_size=sample_size, mic_amount=mic_amount)
    samples = get_samples_from_resources(file_paths, sample_size)
    print(samples)
    random.shuffle(samples)
    print(samples)
    train, valid = samples[:len(samples) - 10], samples[len(samples) - 10:]
    print(len(valid), "asdasd", valid)
    print(len(train), train[0], "\n\n")
    model.fit(train, epochs=500, model_class_epochs=250, model_angle_epochs=1700)
    compiled = model.compile()
    compiled.save("Modern", "3")
    # compiled = ModelPredict.download("60neurs", "5")
    for data_for_validation in (train[:10]):
        print(data_for_validation, compiled.predict_all(data_for_validation.signals))
    pass
    print('#'*30, "\n",'#'*30)
    for data_for_validation in valid:
        print(data_for_validation, compiled.predict_all(data_for_validation.signals))
    pass


if __name__ == '__main__':
    main()
