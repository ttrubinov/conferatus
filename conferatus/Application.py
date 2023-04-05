from Arduino.ArduinoController import ArduinoController
from ML.core.ModelPredict import ModelPredict
from Maths.Fourier import Fourier
from Presenter.Presenter import Presenter

dir_path = ""
prefix = ""
port_micro = "/dev/ttyUSB0"
port_servo = "/dev/ttyUSB1"
data_size = 250


if __name__ == '__main__':
    model_predict = ModelPredict.download(dir_path, prefix)
    presenter = Presenter()
    while True:
        arduino_controller = ArduinoController(1, port=port_micro, data_size=data_size)
        data = arduino_controller.recordData()[0]
        fft = Fourier.fft(data, result_size=100)
        neuro_prediction = model_predict.predict_all(fft)
        print(neuro_prediction)
        if neuro_prediction["class"] == "bad_data":
            print("BAD DATA")
            continue
        res_angle = neuro_prediction["angle"]
        print("Neuro angle: ", res_angle)

        presenter.rotation(res_angle)
