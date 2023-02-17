from abc import ABC, abstractmethod


class MotionSensor(ABC):
    @abstractmethod
    def is_detecting_motion(self) -> bool:
        raise NotImplementedError
