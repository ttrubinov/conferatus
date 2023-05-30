from Arduino.ArduinoController import ArduinoController
from ML.core.ModelPredict import ModelPredict
from Maths.Fourier import Fourier
from Presenter.Presenter import Presenter

dir_path = "2128"
prefix = "maybe"
port_micro = "/dev/ttyUSB0"
port_servo = "/dev/ttyUSB1"
data_size = 250


def addToMediana(lst: list, val):
    i = 0
    while i < 3:
        if val > lst[i]:
            break
        i += 1
    lst.insert(i, val)
    if i < 2:
        lst.pop()
    else:
        lst.pop(0)


def diff():
    presenter = Presenter(port=port_servo)
    arr = [90] * 3
    with ArduinoController(1, port=port_micro, data_size=data_size, baud_rate=19200) as micro_listener:
        while True:
            rd = micro_listener.record_angle()
            if rd is None:
                continue
            # rd = 180-rd
            addToMediana(arr, rd)
            print(f"Angle: {arr[1]}, of {arr} in {arr}")
            presenter.rotation(arr[1])
            # if rd-res > 50:
            #     res += (res-rd)/4
            # else:
            #     res += (res-rd)/2

    pass


def neuro():
    model_predict = ModelPredict.download(dir_path, prefix)
    presenter = Presenter(port=port_servo)
    while True:
        with ArduinoController(1, port=port_micro, data_size=data_size) as arduino_controller:
            data = arduino_controller.recordData()[0]
            fft = Fourier.get_amplitudes_and_phases(data, result_size=100)
            neuro_prediction = model_predict.predict_all(fft)
            print(neuro_prediction)
            if neuro_prediction["class"] == "bad_data":
                print("BAD DATA")
                continue
            res_angle = neuro_prediction["angle"]
            print("Neuro angle: ", res_angle)

            presenter.rotation(res_angle)


import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('asdilfj')
        raise 'где аргументы лебовски'
    match sys.argv[1]:
        case '--neuro':
            neuro()
        case '--diff':
            diff()
        case _:
            raise 'нет такого'
