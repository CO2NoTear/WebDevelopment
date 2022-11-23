from InitTables import user_table
from sqlalchemy.sql import select
from sqlalchemy import desc
from BuildConnection import connection


#s = select(user_table)
#The same as the following one
s = select([user_table.c.UID, user_table.c.UName, user_table.c.UPassword])
#order rearranged by UPassword in dictionary order
s = s.order_by(user_table.c.UPassword)
#Only return top2 of the records
s = s.limit(2)

decrease_order_s = select([user_table.c.UName, user_table.c.UID])
#use desc() to decorate, decreasing order.
decrease_order_s = decrease_order_s.order_by(desc(user_table.c.UName))

rp = connection.execute(s)
rp_desc = connection.execute(decrease_order_s)



##rp.fetchall() will cause rp to be empty
##and result will be a list
#result = rp.fetchall()
#print(type(result))
#print(result)

#first_row = result[0]
#print(first_row[1])
#print(first_row['UName'])
#print(first_row[user_table.c.UName])
#Those three gave the same result: first row and second column of user_table

#rp.first() only return the first line of result, and CLOSE the connection.
#However, it's encouraged if you only need to get the first record
#first_row = rp.first()
#print(first_row)


#before iteration, we can use rp.keys() to see all the keys
print(rp.keys())
#rp is a ResultProxy object, which can be iterable:
for row in rp:
    print(row)

print(rp_desc.keys())
for row in rp_desc:
    print(row)


#Another selection:
#WHERE clause:
s = select([user_table]).where(user_table.c.UName == 'SQESQE')
rp = connection.execute(s)
result = rp.first()
#here result.items() is a func for row obj
print(result.items())
