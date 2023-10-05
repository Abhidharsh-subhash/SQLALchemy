from models import User, Comment
from session import session
from sqlalchemy import select

statement = select(Comment).join(Comment.user).where(
    User.username == 'Abhi').where(Comment.text == 'what is your job?')
result = session.scalars(statement).one()
print(result)
