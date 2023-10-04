from sqlalchemy import insert
from tables import users_table
from connect import engine

# statement = insert(users_table).values(name='Abhi', fullname='Abhidharsh s s')

# with engine.connect() as conn:
#     conn.execute(statement)
#     conn.commit()

statement = insert(users_table)

with engine.connect() as conn:
    conn.execute(statement, [
        {'name': 'Sumesh', 'fullname': 'Sumesh R'},
        {'name': 'Subhash', 'fullname': 'Subhash Sreedharan'}
    ])
    conn.commit()
