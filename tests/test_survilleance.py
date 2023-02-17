
# recorder should stop recording when sensor doesn't detect motion.
# recorder should start recording when sensor detects motion.
# recorder should stop recording when sensor return an unexpected error.
# recorder checks motion every second.

from unittest import TestCase

from assertpy import assert_that
from src.camera import Camera

from src.motion_sensor import MotionSensor
from src.video_recorder import VideoRecorder


class StubSensorWithOutMotion(MotionSensor):
    def is_detecting_motion(self) -> bool:
        return False
    
class StubSensorWithMotion(MotionSensor):
    def is_detecting_motion(self) -> bool:
        return True

class SpyVideoRecorder(VideoRecorder):
    stop_recording_calls = 0
    start_recording_calls = 0
    
    def start_recording(self) -> None:
        self.start_recording_calls += 1
        pass

    def stop_recording(self) -> None:
        self.stop_recording_calls+=1
        pass

class TestCameraShould(TestCase):
    
    def test_stop_recording_when_sensor_doesnt_detect_motion(self):
        stub_sensor = StubSensorWithOutMotion()
        spy_recorder = SpyVideoRecorder()
        camera = Camera(stub_sensor, spy_recorder)
        
        camera.obtain_status()
        
        assert_that(spy_recorder.stop_recording_calls).is_equal_to(1)
    
    def test_start_recording_when_sensor_detect_motion(self):
        stub_sensor = StubSensorWithMotion()
        spy_recorder = SpyVideoRecorder()
        camera = Camera(stub_sensor, spy_recorder)
        
        camera.obtain_status()
        
        assert_that(spy_recorder.start_recording_calls).is_equal_to(1)
    
    # recorder should stop recording when sensor return an unexpected error.