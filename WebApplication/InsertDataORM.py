from InitTablesORM import User, Passage, Comment, Tool, session


user_co2 = User(UName='CO2NoTear',
        UPassword='admin',
        UType=1,
        UIntro='This is a triump for ORM!')
user_zymm = User(UName='zymm',
        UPassword='password',
        UType=1,
        UIntro='test flush')
result = session.query(User).filter(User.UName=='zymm').first()
session.delete(result)
session.commit()
result = session.query(User)
print(result.all())
