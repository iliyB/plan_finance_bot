import os

from dotenv import load_dotenv, find_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker


dotenv_path = find_dotenv()
if dotenv_path:
        load_dotenv(dotenv_path)

SQLALCHEMY_DATABASE_URL = os.environ.get('SQLALCHEMY_DATABASE_URL')

engine = create_async_engine(
        SQLALCHEMY_DATABASE_URL,
        echo=True,
)

async_session = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
)



Base: DeclarativeMeta = declarative_base()
