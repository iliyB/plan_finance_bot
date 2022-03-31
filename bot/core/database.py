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



# expire_on_commit=False will prevent attributes from being expired
# after commit.
async_session = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base: DeclarativeMeta = declarative_base(class_registry={"UserCategory": UserCategory})
Base: DeclarativeMeta = declarative_base()
