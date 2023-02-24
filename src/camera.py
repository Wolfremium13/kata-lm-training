import time

from src.motion_sensor import MotionSensor
from src.video_recorder import VideoRecorder


class Camera:
    def __init__(self, motion_sensor: MotionSensor, video_recorder: VideoRecorder):
        self.motion_sensor = motion_sensor
        self.video_recorder = video_recorder

    def obtain_status(self, number_of_calls=1):
        calls = 0
        wait_time = 1
        while calls < number_of_calls:
            self._update_status()
            time.sleep(wait_time)
            calls += 1

    def _update_status(self):
        if self.motion_sensor.is_detecting_motion():
            self.video_recorder.start_recording()
        else:
            self.video_recorder.stop_recording()
