import math
import time

import serial

def batched(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]

class ArduinoController:
    def __init__(self, batch_size: int, baud_rate=230400, port: str = f"COM3", data_size=250):
        self.data_size = data_size
        self.batch_size = batch_size
        self.port = port
        self.baud_rate = baud_rate
        self.serial = None

    def __enter__(self):
        self.serial = serial.Serial(self.port, self.baud_rate, timeout=2)
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.serial.close()

    def recordData(self, batch_size: int = None, port: str = None) -> list[list[list[float]]]:
        if batch_size is None:
            batch_size = self.batch_size
        if port is not None:
            self.serial.close()
            self.serial = serial.Serial(port, self.baud_rate, timeout=2)
        ser = self.serial
        print("started")


        arr = []
        for i in range(0, batch_size):
            ser.write(b'c\n')

            while not ("S" in (a := ser.readline().decode())):
                print(a)
                time.sleep(1)
                ser.write(b'c')
                print("Waiting")
            for j in range(self.data_size):
                line = ser.readline()  # read a byte
                if line:
                    arr.append(line)
            while not ("E" in ser.readline().decode()):
                print("Wait")
        
        answer = []
        for batch in batched(arr, self.data_size):
            sample = [[], [], []]
            for line in batch:
                line = map(float, line.decode().strip().split())
                for index, value in enumerate(line):
                    sample[index].append(value)
            answer.append(sample)
        return answer
        # for sample in range(0, batch_size):
        #     for line in range(0, data_size):
        #         answer = map(float, line.decode().strip().split())
        #         for index, value in enumerate(line):
        #             answer[index].append(value)
        # return answer
    def record_angle(self) -> float:
        ser = self.serial
        ser.write(b'c\n')

        while not ("S" in (a := ser.readline().decode())):
            print(a)
            ser.write(b'c')
            time.sleep(1)
            print("Waiting")
        while True:
            line = ser.readline()
            print(f"Why? {line}")
            if line:

                res = float(line.decode().strip())

                if math.isnan(res):
                    return None
                return round(res)
            else:
                return None





if __name__ == '__main__':
    with ArduinoController(3, baud_rate=230400, port="COM3") as controller:
        print(controller.recordData(2))
