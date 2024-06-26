from sqlalchemy import BigInteger, String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from dotenv import load_dotenv
import os

load_dotenv()
engine = create_async_engine(url=os.getenv('POSTGRES'))

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id = mapped_column(BigInteger, primary_key=True, autoincrement=False)
    created_at = mapped_column(DateTime)
    status: Mapped[str] = mapped_column(String(10))
    status_updated_at = mapped_column(DateTime)
    send_message_at = mapped_column(DateTime)
    send_message_num: Mapped[int] = mapped_column()


class Trigger(Base):
    __tablename__ = 'triggers'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id = mapped_column(BigInteger)
    message_id = mapped_column(BigInteger)


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
