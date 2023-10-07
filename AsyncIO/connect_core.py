from sqlalchemy import Table, Column, Integer, MetaData, String, Text
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import select
import asyncio

# installation
# pip install sqlalchemy[asyncio] aiosqlite
# asyncpg for postgresql
# asyncmysql for mysql

meta = MetaData()

users_table = Table(
    'users',
    meta,
    Column('id', Integer, primary_key=True),
    Column('username', String, nullable=False),
    Column('email', String, nullable=False),
    Column('bio', Text, nullable=False)
)


async def async_main():
    engine = create_async_engine(
        'sqlite+aiosqlite:///sample.db',
        echo=True
    )
    # connected
    async with engine.begin() as conn:
        # create db
        await conn.run_sync(meta.create_all)
        # insert data into table
        await conn.execute(users_table.insert(), [
            {'username': 'Abhi', 'email': 'abhidharsh6@gmail.com',
                'bio': 'I am a delivery boy'},
            {'username': 'Abhidharsh', 'email': 'abhidharsh1999@gmail.com',
                'bio': 'I am a Python developer'}
        ])
    async with engine.connect() as conn:
        statement = select(users_table).where(users_table.c.username == 'Abhi')
        result = await conn.execute(statement)
        print(result.all())

    # for closing a connection
    await engine.dispose()

asyncio.run(async_main())
