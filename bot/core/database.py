from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from bot.config import configs

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://{}:{}@{}:{}/{}".format(
    configs.POSTGRES_USER,
    configs.POSTGRES_PASSWORD,
    configs.POSTGRES_HOST,
    configs.POSTGRES_PORT,
    configs.POSTGRES_DB,
)

Base = declarative_base()


class Database:
    __instance = None

    def __init__(self) -> None:
        if not Database.__instance:
            self.engine = create_async_engine(
                SQLALCHEMY_DATABASE_URL,
                echo=True,
            )

            self.async_session = sessionmaker(
                self.engine, expire_on_commit=False, class_=AsyncSession
            )

    @classmethod
    def getInstance(cls) -> object:
        if not cls.__instance:
            cls.__instance = Database()
        return cls.__instance


def get_async_session() -> sessionmaker:
    return Database().async_session()


def get_engine() -> sessionmaker:
    return Database().async_session()
