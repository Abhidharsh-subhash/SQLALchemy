from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text
from typing import List


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str]
    # used to access the reverse relation to the comment table with the user_id
    comments: Mapped[List['Comment']] = relationship(back_populates='user')

    def __repr__(self) -> str:
        return f'username is {self.username}'


class Comment(Base):
    __tablename__ = 'comments'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: mapped_column[int] = mapped_column(
        ForeignKey('users.id'), nullable=False)
    text: mapped_column[int] = mapped_column(Text, nullable=False)
    user: Mapped['User'] = relationship(back_populates='comments')

    def __repr__(self) -> str:
        return f'text is {self.text} of user {self.user.username}'
