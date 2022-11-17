from sqlalchemy import insert
from BuildConnection import connection
from InitTables import user_table, passage_table, tool_table, comment_table

class User:
    def __init__(self, name, password, intro,
            moto="", level=1, exp=0,
            user_type=0, passage_num=0):
        self.name = name
        self.password = password
        self.moto = moto
        self.level = level
        self.exp = exp
        self.user_type = user_type
        self.intro = intro
        self.passage_num = passage_num
    def insertData(self, connection, debug=False):
        ins = insert(user_table).values(
                UName=self.name,
                UPassword=self.password,
                UMoto=self.moto,
                ULevel=self.level,
                UExp=self.exp,
                UType=self.user_type,
                UIntro=self.intro,
                UPNum=self.passage_num
                )
        if debug == True:
            print(ins.compile().params)
        connection.execute(ins)


userCO2 = User("CO2NoTear",'admin',level=6,exp=114514,user_type=1,intro='This was a triump.')
userCO2.insertData(connection=connection, debug=True)
