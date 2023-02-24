

from unittest import TestCase

from assertpy import assert_that

from src.repository import Repository
from src.user import User

# API Repository -> User -> Repository Impl -> In Memory DB

# - Validar si el usuario existe
# - Validar el correo

class RepositoryDatabaseInMemory(Repository):
    users: list[User] = []
    
    def save(self, user: User) -> None:
        self.users.append(user)
    
    def get_user(self, username: str) -> User:
        return [u for u in self.users if u.username == username][0]
    

class TestRepositoryShould(TestCase):
        
    def test_save_in_database(self):
        repository = RepositoryDatabaseInMemory()
        username = "leto"
        given_user = User(username, "password", "email")
        
        repository.save(given_user)
        expected_user = repository.get_user(username)
        
        assert_that(given_user).is_equal_to(expected_user)
    
    