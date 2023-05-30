import time
import serial


class MotionController:
    def __init__(self, baud_rate=230400, port: str = f"/dev/ttyUSB0"):
        self.port = port
        self.baud_rate = baud_rate
        self.ser = serial.Serial(self.port, self.baud_rate, timeout=6)

    def move(self, angle: int) -> None:
        self.ser.write((180 - angle).to_bytes(1, 'little'))
        time.sleep(1)

