from abc import ABC, abstractmethod

from src.user import User


class Repository(ABC):
    @abstractmethod
    def save(self, user: User) -> None:
        pass

    @abstractmethod
    def get_user(self, username: str) -> User:
        pass
