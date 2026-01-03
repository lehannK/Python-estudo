from sqlmodel import Sequence, Session
from sqlmodel import select
from app.modules.models import User


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def find_all(self) -> Sequence[User]:
        statement = select(User)  # equivale ao "SELECT * FROM users"
        results = self.session.exec(statement)  # executa a query
        return results.all()  # retorna todos os resultados como uma lista

    def create(self, user: User) -> User:
        try:
            self.session.add(user)
            self.session.commit()
            self.session.refresh(user)
            return user
        except Exception as e:
            self.session.rollback()
            raise ValueError(f"Erro ao criar usuário: {str(e)}")

    def find_by_email(self, email: str) -> User | None:
        statement = select(User).where(User.email == email)
        result = self.session.exec(statement).first()
        return result

    def find_by_cpf(self, cpf: str) -> User | None:
        statement = select(User).where(User.cpf == cpf)
        result = self.session.exec(statement).first()
        return result
