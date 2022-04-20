import os

from dotenv import find_dotenv, load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

from bot import config

dotenv_path = find_dotenv()
if dotenv_path:
    load_dotenv(dotenv_path)
    SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://{}:{}@localhost:5431/{}".format(
        os.environ.get("POSTGRES_USER"),
        os.environ.get("POSTGRES_PASSWORD"),
        os.environ.get("POSTGRES_DB"),
    )
else:
    SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://{}:{}@{}:{}/{}".format(
        config.POSTGRES_USER,
        config.POSTGRES_PASSWORD,
        config.POSTGRES_HOST,
        config.POSTGRES_PORT,
        config.POSTGRES_DB,
    )

Base: DeclarativeMeta = declarative_base()


class Database:
    __instance = None

    def __init__(self) -> None:
        if not Database.__instance:
            self.engine = create_async_engine(
                SQLALCHEMY_DATABASE_URL,
                echo=False,
            )

            self.async_session = sessionmaker(self.engine, expire_on_commit=False, class_=AsyncSession)

    @classmethod
    def getInstance(cls) -> object:
        if not cls.__instance:
            cls.__instance = Database()
        return cls.__instance


def get_async_session() -> sessionmaker:
    return Database().async_session()


def get_engine() -> sessionmaker:
    return Database().async_session()
