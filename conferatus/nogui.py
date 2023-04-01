from raytracing.Plotter import Plotter
from raytracing.Fourier import Fourier
from raytracing.ArduinoController import ArduinoController


with ArduinoController(batch_size = 5, port = "/dev/ttyUSB0") as arduinoController:
    data = arduinoController.recordData()

    for i in range(0, 5):
        fourierSample = Fourier.get_amplitudes_and_phases(data[i])
        # for i in fourierSample:
        #     print(i)
        print(fourierSample)

        Plotter.draw(y_axis=fourierSample)