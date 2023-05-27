import itertools
import random

from conferatus.ML.Datasets.Dataset import Sample, Dataset
from conferatus.ML.core.ModelLearning import ModelLearning
from conferatus.ML.core.ModelPredict import ModelPredict


def get_samples_from_resources(file_paths: list, max_data=None) -> list[Sample]:
    arr: list[list[Sample]] = []
    for file_path in file_paths:
        samples: list[Sample] = Dataset.get_samples(file_path)
        for i in range(len(samples)):
            for j in range(0, len(samples[i].signals)):
                samples[i].signals[j] = samples[i].signals[j][:max_data]
        arr.append(samples)
    lst = list(itertools.chain.from_iterable(arr))
    random.shuffle(lst)
    return lst


def main():
    file_paths = [
        # "freqDataSet.json",
        # "freakNewDataSet.json",
        # "freakThirdDataSet.json",
        # "BreakingBadData.json",
        # "0905.json",
        # "0905_voice.json",
        # "improvedfreq.json",
        # "improvedvoice.json",
        # "improvedclap.json",

        "2128_2.json",
        "2128_2_baddata.json",
        "2128_2_cholopok.json",
        "2128_2_person.json",
    ]
    mic_amount = 3
    sample_size = 100
    model = ModelLearning(sample_size=sample_size, mic_amount=mic_amount)
    samples = get_samples_from_resources(file_paths, sample_size)
    train, valid = samples[:len(samples) - 20], samples[len(samples) - 20:]
    print(len(valid), "asdasd", valid)
    print(len(train), train[0], "\n\n")
    model.fit(train, frequency_epochs=500, person_epochs=1100, class_epochs=900, angle_epochs=1400)
    compiled = model.compile()
    compiled.save("2128", "newAll4")
    compiled = ModelPredict.download("2128", "newAll4")
    for data_for_validation in (train[:20]):
        print(data_for_validation, compiled.predict_all(data_for_validation.signals))

    print('#' * 30, "\n", '#' * 30)

    for data_for_validation in valid:
        print(data_for_validation, compiled.predict_all(data_for_validation.signals))
    pass


if __name__ == '__main__':
    main()