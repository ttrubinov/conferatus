class MotionController:
    def __init__(self, start_angle: float = 0, coefficient: float = 1):
        self.angle = start_angle
        self.coefficient = coefficient

    def __update_with_new_value(self, new_value: float):
        self.angle = self.coefficient * new_value + (1 - self.coefficient) * self.angle

    def __get_new_value(self):
        return self.angle

    def whether_to_spin(self, new_angle: float) -> bool:
        self.__update_with_new_value(new_angle)
        final_angle = self.__get_new_value()
        if abs(self.angle - final_angle) < 15:
            return False
        return True

    def get_new_rotation_angle(self):
        self.__get_new_value()
        return self.angle
