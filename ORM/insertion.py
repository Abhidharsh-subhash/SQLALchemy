from models import User, Comment
from session import session

user1 = User(
    username='Abhi',
    email='abhi@gmail.com',
    comments=[
        Comment(text='how are you?'),
        Comment(text='what is your job?')
    ]
)
user2 = User(
    username='Abhidharsh s s',
    email='abhidharsh6@gmail.com',
    comments=[
        Comment(text='you are great'),
        Comment(text='you have good skills')
    ]
)
user3 = User(
    username='Abhilash s',
    email='abhisubhash@gmail.com',
    comments=[
        Comment(text='He is a ssc student'),
        Comment(text='he is a swiggy driver')
    ]
)
# if there is only single data to insert then we use add
session.add_all([user1, user2, user3])
session.commit()
