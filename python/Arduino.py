import time

import serial


class ArduinoController:
    def __init__(self, com_port, baud_rate, sample_size, data_size=250):
        self.data_size = data_size
        self.sample_size = sample_size
        self.com_port = f"COM{com_port}"
        self.baud_rate = baud_rate
        self.serial = None

    def __enter__(self):
        self.serial = serial.Serial(self.com_port, self.baud_rate, timeout=2)
        return self

    def __exit__(self, type, value, traceback):
        self.serial.close()

    def recordSample(self, angle):
        arr = []
        ser = self.serial
        print("started")
        for i in range(0, self.sample_size):
            ser.write(b'c\n')
            while not ("S" in ser.readline().decode()):
                time.sleep(1)
                ser.write(b'c')
                print("Waiting")
            for j in range(self.data_size):
                line = ser.readline()  # read a byte
                if line:
                    arr.append(line)
            while not ("E" in ser.readline().decode()):
                print("Wait")
        answer = [[], [], []]
        for line in arr:
            line = map(float, line.decode().strip().split())
            for index, value in enumerate(line):
                answer[index].append(value)
        return {
            "angle": angle,
            "signals": answer
        }


if __name__ == '__main__':
    with ArduinoController(3, 230400, 1) as controller:
        print(controller.recordSample(45))
