from tables import users_table
from connect import engine
from sqlalchemy import select

# statement = select(users_table)  it will return all the datas in the table
# it is used for the filtering the data's in the users table
statement = select(users_table).where(users_table.c.name == 'Abhi')
with engine.connect() as conn:
    result = conn.execute(statement)
    for row in result:
        # print(row)
        print(f"name={row.name}, fullname={row.fullname}")
