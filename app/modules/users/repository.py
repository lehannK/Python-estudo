from sqlmodel import Sequence, Session
from sqlmodel import select
from app.modules.models import Users


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def find_all(self) -> Sequence[Users]:
        statement = select(Users)  # equivale ao "SELECT * FROM users"
        results = self.session.exec(statement)  # executa a query
        return results.all()  # retorna todos os resultados como uma lista
