import serial


class MotionController:
    def __init__(self, baud_rate=230400, port: str = f"COM3"):
        self.port = port
        self.baud_rate = baud_rate
        self.serial = serial.Serial(self.port, self.baud_rate, timeout=2)

    def move(self, angle: int) -> None:
        self.serial.write((180 - angle).to_bytes(1, 'little'))
