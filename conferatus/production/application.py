from conferatus.Arduino.ArduinoController import ArduinoController
from conferatus.ML.core.ModelPredict import ModelPredict

dir_path = ""
prefix = ""
port = ""
data_size = 250


if __name__ == '__main__':
    model_predict = ModelPredict.download(dir_path, prefix)
    while True:
        arduino_controller = ArduinoController(1, port=port, data_size=data_size)
        sample = arduino_controller.recordData()[0]



