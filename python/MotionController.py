class MotionController:
    def __init__(self, angle: float = 0):
        self.angle = angle
        self.prev_angles = [0.0]

    def get_new_rotation_angle(self, new_angle: float) -> float:
        if len(self.prev_angles) > 9:
            self.prev_angles.pop(0)
            self.prev_angles.append(new_angle)

        final_angle = sum(self.prev_angles) / len(self.prev_angles)

        if abs(self.angle - final_angle) < 15:
            return 0
        else:
            self.angle = final_angle
            return self.angle
