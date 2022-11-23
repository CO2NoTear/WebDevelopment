from InitTables import user_table, cookies, passage_table, comment_table, tool_table
from BuildConnection import connection

ins = user_table.insert().values(
        UName='CO2NoTear',
        UPassword='admin',
        UType=1,
        UIntro='This was a triump',
        )
print(ins.compile().params)
to_be_insert_data_list = [
        {
            'UName' : 'SQESQE',
            'UPassword' : 'password1',
            'UType' : 0,
            'UIntro' : 'Can I insert 2 of the records?'
            },
        {
            'UName' : 'YourDad',
            'UPassword' : 'Nopassword',
            'UType' : 0,
            'UIntro' : 'Are you kidding me?'
            }
        ]

result = connection.execute(ins, to_be_insert_data_list)
