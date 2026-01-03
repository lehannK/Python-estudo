from sqlmodel import create_engine, Session
from app.core.config import settings

engine = create_engine(
    settings.database_url,
    echo=True  # log SQL no terminal (dev)
)


def get_session():
    with Session(engine) as session:
        yield session
