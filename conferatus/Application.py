from Arduino.ArduinoController import ArduinoController
from ML.core.ModelPredict import ModelPredict
from Maths.Fourier import Fourier
from Presenter.Presenter import Presenter

dir_path = "2128"
prefix = "maybe"
port_micro = "COM4"
port_servo = "COM7"
data_size = 250
def anotherParasha():
    presenter = Presenter(port=port_servo)
    res = 90
    arr = [90]*3
    with ArduinoController(1, port=port_micro, data_size=data_size, baud_rate=19200) as micro_listener:
        while True:
            rd = micro_listener.record_angle()
            if rd is None:
                continue
            # rd = 180-rd
            arr.pop(0)
            arr.append(rd)
            print(f"Angle: {sorted(arr)[1]}, of {sorted(arr)} in {arr}")
            presenter.rotation(sorted(arr)[1])
            # if rd-res > 50:
            #     res += (res-rd)/4
            # else:
            #     res += (res-rd)/2

    pass

def main():
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
if __name__ == '__main__':
    # main()
    anotherParasha()