from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text, select, delete
from typing import List
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    bio: Mapped[str] = mapped_column(nullable=False)
    # used to access the reverse relation to the comment table with the user_id
    comments: Mapped[List['Comment']] = relationship(back_populates='user')

    def __repr__(self) -> str:
        return f'username is {self.username}'


class Comment(Base):
    __tablename__ = 'comments'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'), nullable=False)
    text: Mapped[int] = mapped_column(Text, nullable=False)
    user: Mapped['User'] = relationship(back_populates='comments')

    def __repr__(self) -> str:
        return f'text is {self.text} of user {self.user.username}'

# insert data


async def insert_data(sessionmaker: async_sessionmaker[AsyncSession]):
    async with sessionmaker() as session:
        async with session.begin():
            session.add_all([
                User(
                    username='abhi',
                    email='abhi@gmail.com',
                    bio='Python developer',
                    comments=[
                        Comment(text='seeking for opportunities'),
                        Comment(text='A self-learned developer'),
                    ]
                ),
                User(
                    username='abhi123',
                    email='abhi@123',
                    bio='Python developer with 1 year of experience',
                )
            ])

            session.commit()

# selecting,update and deleting


async def select_update(sessionmaker: async_sessionmaker[AsyncSession]):
    async with sessionmaker() as session:
        statement = select(User).where(User.username == 'abhidharsh')
        result = await session.execute(statement)
        # print(result.all())
        # print(result.scalars().one())
        user = result.scalars().one()
        # user.username = 'abhidharsh' it is for updating
        await session.delete(user)
        await session.commit()


async def async_main():
    # create the engine
    engine = create_async_engine(
        'sqlite+aiosqlite:///sample2.db',
        echo=True
    )

    # create a session which will be used to interact with the database
    session = async_sessionmaker(bind=engine, expire_on_commit=False)

    # creating connection to our database
    async with engine.begin() as conn:
        # create db tables
        # await conn.run_sync(Base.metadata.create_all)
        # await insert_data(session)
        await select_update(session)

asyncio.run(async_main())
