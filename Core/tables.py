from sqlalchemy import Table, MetaData, Column
from sqlalchemy import Integer, String, Text, ForeignKey

meta_obj = MetaData()
# The metadata object is going to keep the information about all the tables right here

'''users table:
    -id pk
    -name str
    -fullname str
    -email
'''
users_table = Table(
    'users',
    meta_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String(25), nullable=False),
    Column('fullname', Text)
)

'''comments table:
    -id pk
    -comment str
    -user_id int > users.id
'''
comments_table = Table(
    'comments',
    meta_obj,
    Column('id', Integer, primary_key=True),
    Column('comment', Text, nullable=False),
    Column('user_id', ForeignKey('users.id'))
)
