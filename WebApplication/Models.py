from app import db
from sqlalchemy.ext.automap import automap_base
from BuildConnection import engine

#use automap_base to create all ORM objects from existed table
Base = automap_base()
Base.prepare(engine=engine, reflect=True)

print(Base.classes.keys())
#user_table is an ORM obj
user_table = Base.classes.USR
passage_table = Base.classes.PSG
comment_table = Base.classes.CMT
tool_table = Base.classes.TOL
