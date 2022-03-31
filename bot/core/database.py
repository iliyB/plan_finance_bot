import os

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@{}:{}/{}".format(
        os.environ.get('POSTGRES_USER'),
        os.environ.get('POSTGRES_PASSWORD'),
        os.environ.get('DB_CONTAINER_NAME'),
        os.environ.get('POSTGRES_PORT'),
        os.environ.get('POSTGRES_DB')
)

# engine = create_engine(SQLALCHEMY_DATABASE_URL)
engine = create_async_engine(
        "postgresql+asyncpg://scott:tiger@localhost/test",
        echo=True,
)



# expire_on_commit=False will prevent attributes from being expired
# after commit.
async_session = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base: DeclarativeMeta = declarative_base()

async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
