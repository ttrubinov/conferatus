import time
import serial


class MotionController:
    def __init__(self, baud_rate=9600, port: str = f"/dev/ttyUSB1"):
        self.port = port
        self.baud_rate = baud_rate
        self.ser = serial.Serial(self.port, self.baud_rate, timeout=2)

    def move(self, angle: int) -> None:
        self.ser.write((180 - angle).to_bytes(1, 'little'))
        print((180 - angle).to_bytes(1, 'little'))
        print(self.ser.readline())
        time.sleep(2)

# a = MotionController()

# while True:
#     a.move(90)
#     a.move(180)