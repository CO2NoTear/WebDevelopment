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
# user1 = session.query(User).first()
# print(user1)
# passage1 = Passage(
#     PTitle = 'First Passage',
#     PContent = '# Hello, markdown.',
#     PAbstract = "First Passage's abstract",
#     PUID = user1.UID
# )
# session.add(passage1)
# comment1 = Comment(
#     CUID = user1.UID,
#     CPID = passage1.PID,
#     CContent = 'First comment'
# )
passage2 = Passage(
    PTitle = 'Second Passage',
    PContent = '# Hello, markdown.',
    PAbstract = "Second Passage's abstract",
    PUID = 1
)
# session.add(passage2)
# session.commit()
result = session.query(Passage).filter(Passage.PTitle.like("%Second%"))
print(result.all())
