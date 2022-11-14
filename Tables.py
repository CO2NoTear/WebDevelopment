from datetime import datetime
from sqlalchemy import Integer, String, Text, Boolean, DateTime, Column, MetaData, ForeignKey, Table, Numeric

metadata = MetaData()

cookies = Table('cookies', metadata,
                Column('cookie_id', Integer(), primary_key=True),
                Column('cookie_name', String(50), index=True),
                Column('cookie_recipe_url', String(255)),
                Column('cookie_sku', String(55)),
                Column('quantity', Integer()),
                Column('unit_cost', Numeric(12,2))
                )

passage_table = Table('PSG', metadata,
                    Column('PID', Integer(), primary_key=True),
                    Column('PTitle', String(255), nullable=False),
                    Column('PType', Boolean(), nullable=False, default=1),
                    Column('PUID', ForeignKey('UID')),
                    Column('PAbstruct', String(1024), nullable=False),
                    Column('PContent', Text(), nullable=False),
                    Column('PLink', String(1024)),
                    Column('PTag', String(255)),
                    Column('PPermission', Integer(), nullable=False, default=0),
                    Column('PCNum', Integer(), nullable=False, default=0),
                    Column('PLikes', Integer(), nullable=False, default=0),
                    Column('PSubdate', DateTime(), default=datetime.now())
                    )
user_table = Table('USR', metadata,
                    Column('UID', Integer(), primary_key=True),
                    Column('UName', String(64), nullable=False, unique=True, index=True),
                    Column('UPassword', String(256), nullable=False),
                    Column('UMoto', String(256), nullable=False, default='Lazy guy with nothing left here.'),
                    Column('ULevel', Integer(), nullable=False, default=1),
                    Column('UExp', Integer(), nullable=False,default=0),
                    Column('UType', Integer(), )
                    )