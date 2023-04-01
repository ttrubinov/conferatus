from raytracing.Plotter import Plotter
from raytracing.Fourier import Fourier
from raytracing.ArduinoController import ArduinoController


with ArduinoController(batch_size = 2, port = "/dev/ttyUSB0") as arduinoController:
    data = arduinoController.recordData()

for i in range(0, 2):
    fourierSample = Fourier.get_amplitudes_and_phases(data[i])
    Plotter.draw(y_axis=fourierSample, color = ['red', 'blue', 'green'])
    # print(fourierSample)

        