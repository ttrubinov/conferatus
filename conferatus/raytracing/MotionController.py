class MotionController:
    def __init__(self, start_angle: float = 0, coefficient: float = 0.5):
        self.angle = start_angle
        self.coefficient = coefficient

    def __get_new_value(self):
        return self.angle

    def update_with_new_value(self, new_value: float):
        self.angle = self.coefficient * new_value + (1 - self.coefficient) * self.angle

    def whether_to_spin(self) -> bool:
        final_angle = self.__get_new_value()
        if abs(self.angle - final_angle) < 15:
            return False
        return True

    def get_new_rotation_angle(self):
        return self.__get_new_value()
