from InitTables import user_table, cookies, passage_table, comment_table, tool_table
from BuildConnection import connection

ins = user_table.insert().values(
        UName='CO2NoTear',
        UPassword='admin',
        UType=1,
        UIntro='This was a triump',
        )
print(ins.compile().params)


result = connection.execute(ins)
