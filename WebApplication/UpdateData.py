from sqlalchemy import update
from BuildConnection import connection
from InitTables import user_table

u = update(user_table).where(user_table.c.UName == 'SQESQE')
u = u.values(UExp = (user_table.c.UExp + 123))
result = connection.execute(u)
