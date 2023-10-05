from session import session
from models import User, Comment

comment = session.query(Comment).filter_by(id=6).first()
session.delete(comment)
session.commit()
