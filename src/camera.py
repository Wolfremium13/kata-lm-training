
from src.motion_sensor import MotionSensor
from src.video_recorder import VideoRecorder


class Camera():
    def __init__(self, motion_sensor: MotionSensor, video_recorder: VideoRecorder):
        self.motion_sensor = motion_sensor
        self.video_recorder = video_recorder
    
    def obtain_status(self):
        if self.motion_sensor.is_detecting_motion():
            self.video_recorder.start_recording()
        else:
            self.video_recorder.stop_recording()
        