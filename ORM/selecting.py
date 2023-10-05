from models import User, Comment
from connect import engine
from sqlalchemy import select
from session import session

# statement = select(User).where(User.username.in_(['Abhi', 'Abhidharsh s s']))
# result = session.scalar(statement)
# print(result)

# it is for selection the whole datas in the table User
# users = session.query(User).all()
# for user in users:
#     print(user)

user = session.query(User).filter_by(username='Abhidharsh s s').first()
# user = session.query(User).filter(User.username == 'Abhidharsh s s') #filter is used when there is more complexity in the conditions
print(user)
