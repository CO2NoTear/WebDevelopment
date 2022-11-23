from sqlalchemy.sql import func, select
from BuildConnection import connection
from InitTables import user_table

#Simple sum function
s = select([func.sum(user_table.c.UExp).label('exp_sum')])
rp = connection.execute(s)

#we used label to rename the column.
print(rp.keys())
#get the first val of the sum. sum is a single column vector, so it's leagal.
print(rp.scalar())
