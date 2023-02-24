

from unittest import TestCase
from assertpy import assert_that

from src.repository import Repository
from src.user import User



# API Repository -> User -> Repository Impl -> In Memory DB

# - Validar si el usuario existe
# - Validar el correo

class RepositorySpy(Repository):
    _user_save = None
    def save(self, user: User) -> None:
        self._user_save = user
    
    def get_user(self, user_name: str) -> User:
        pass
    
    def assert_user_is_saved(self, user: User) -> None:
        assert_that(self._user_save).is_equal_to(user)
    

class TestRepositoryShould(TestCase):
    
    def test_save_user(self):
        repository = RepositorySpy()
        user = User("username", "password", "email")
        
        repository.save(user)

        repository.assert_user_is_saved(user)
        
    def test_save_in_database(self):
        repository = RepositoryDatabase()
        username = "leto"
        given_user = User(username, "password", "email")
        
        repository.save(given_user)
        expected_user = repository.get_user(username)
        
        assert_that(given_user).is_equal_to(given_user)
        
        
        