class MotionService:
    def __init__(self, start_angle: float = 0, coefficient: float = 1):
        self.angle = start_angle
        self.coefficient = coefficient

    def __get_value(self) -> float:
        return self.angle

    def update_value(self, new_value: float) -> None:
        self.angle = self.coefficient * new_value + (1 - self.coefficient) * self.angle

    def should_rotate(self) -> bool:
        # if abs(self.angle - self.__get_value()) < 15:
        #     return False
        return True

    def get_rotation_angle(self) -> int:
        if self.__get_value() < 30:
            return 30
        elif self.__get_value() > 150:
            return 150
        else:
            return round(self.__get_value())
