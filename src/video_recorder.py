from abc import ABC, abstractmethod


class VideoRecorder(ABC):
    @abstractmethod
    def start_recording(self) -> None:
        raise NotImplementedError
    @abstractmethod
    def stop_recording(self) -> None:
        raise NotImplementedError
