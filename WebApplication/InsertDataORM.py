from InitTablesORM import User, Passage, Comment, Tool, session


user_co2 = User(UName='CO2NoTear',
        UPassword='admin',
        UType=1,
        UIntro='This is a triump for ORM!')
user_zymm = User(UName='zymm',
        UPassword='password',
        UType=1,
        UIntro='test flush')
session.add(user_co2)
session.commit()
result = session.query(User)
print(result.all())
