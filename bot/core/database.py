import sys

from config import configs
from py_singleton import singleton
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# sys.path = ['', 'bt'] + sys.path[1:]


SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://{}:{}@{}:{}/{}".format(
    configs.POSTGRES_USER,
    configs.POSTGRES_PASSWORD,
    configs.POSTGRES_HOST,
    configs.POSTGRES_PORT,
    configs.POSTGRES_DB,
)

Base = declarative_base()


@singleton
class Database:
    engine = create_async_engine(
        SQLALCHEMY_DATABASE_URL,
        echo=False,
    )
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


def get_async_session() -> AsyncSession:
    return Database().async_session()
