from Motion.MotionController import MotionController
from Motion.MotionService import MotionService


class Presenter:
    def __init__(self, baud_rate=230400, port="COM5") -> None:
        self.motion_service = MotionService()
        self.motion_controller = MotionController(baud_rate=baud_rate,port=port)

    def rotation(self, angle: int):
        self.motion_service.update_value(angle)
        if self.motion_service.should_rotate():
            new_angle = self.motion_service.get_rotation_angle()
            # print("Result angle: ", new_angle)
            self.motion_controller.move(new_angle)
