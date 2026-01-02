from .repository import UserRepository


def get_user_service():
    repo = UserRepository()
    return UserService(repo)


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def list_users(self):
        return self.repo.find_all()
