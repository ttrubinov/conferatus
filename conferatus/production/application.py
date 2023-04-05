from conferatus.conferatus.Arduino.ArduinoController import ArduinoController
from conferatus.conferatus.ML.core.ModelPredict import ModelPredict
from conferatus.conferatus.Maths.Fourier import Fourier
from conferatus.conferatus.Presenter.Presenter import Presenter

dir_path = ""
prefix = ""
port = ""
data_size = 250


if __name__ == '__main__':
    model_predict = ModelPredict.download(dir_path, prefix)
    presenter = Presenter()
    while True:
        arduino_controller = ArduinoController(1, port=port, data_size=data_size)
        data = arduino_controller.recordData()[0]
        fft = Fourier.fft(data, result_size=100)
        neuro = model_predict.predict_all(fft)
        print(neuro)
        if neuro["class"] == "bad_data":
            print("BAD DATA")
            continue
        res_angle = neuro["angle"]
        presenter.rotation(res_angle)
