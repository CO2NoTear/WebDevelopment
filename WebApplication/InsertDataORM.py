from ast import Pass
from InitTablesORM import User, Passage, Comment, Tool, session


# user_co2 = User(UName='CO2NoTear',
#         UPassword='admin',
#         UType=1,
#         UIntro='This is a triump for ORM!')
# user_zymm = User(UName='zymm',
#         UPassword='password',
#         UType=1,
#         UIntro='test flush')
# session.add(user_co2)
# passage1 = Passage(
#     PTitle = 'First Passage',
#     PContent = '# Hello, markdown.',
#     PAbstract = "First Passage's abstract"
# )
# session.add(passage1)
user1 = session.query(User).filter(User.UID==1).first()
passage1 = session.query(Passage).filter(Passage.PID==1).first()
comment1 = Comment(
    CUID = user1.UID,
    CPID = passage1.PID,
    CContent = 'First comment'
)
session.add(comment1)
session.commit()
result = session.query(Comment)
print(result.all())
