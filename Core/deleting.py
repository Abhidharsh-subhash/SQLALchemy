from connect import engine
from tables import users_table
from sqlalchemy import delete

statement = delete(users_table).where(users_table.c.name == 'Subhash')

with engine.connect() as conn:
    conn.execute(statement)
    conn.commit()
