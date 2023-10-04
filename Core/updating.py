from connect import engine
from tables import users_table
from sqlalchemy import update

statement = update(users_table).where(users_table.c.name ==
                                      'Abhi').values(fullname='Abhidharsh')

with engine.connect() as conn:
    conn.execute(statement)
    conn.commit()
