from datetime import datetime
from sqlalchemy import \
        Integer, String, Text, Boolean, \
        DateTime, Column, MetaData, ForeignKey, \
        Table, Numeric
from BuildConnection import engine

metadata = MetaData()

#不知道有什么用的cookie表
cookies = Table('cookies', metadata,
                Column('cookie_id', Integer(), primary_key=True),
                Column('cookie_name', String(50), index=True),
                Column('cookie_recipe_url', String(255)),
                Column('cookie_sku', String(55)),
                Column('quantity', Integer()),
                Column('unit_cost', Numeric(12,2))
                )

#用户表，主键：UID
#无外键。 UID作为其他表的重要外键。
#UName 添加了索引
user_table = Table('USR', metadata,
                    Column('UID', Integer(), primary_key=True),
                    Column('UName', String(64), nullable=False, unique=True, index=True),
                    Column('UPassword', String(256), nullable=False),
                    Column('UMoto', String(256), nullable=False, default='Lazy guy with nothing left here.'),
                    Column('ULevel', Integer(), nullable=False, default=1),
                    Column('UExp', Integer(), nullable=False,default=0),
                    Column('UType', Integer(), nullable=False, default=0),
                    Column('UIntro', Text(), nullable=False),
                    Column('UPNum', Integer(),default=0,nullable=False)
                    )

# 文章表，PUID以UID作为外键
# 不知道PLink要怎么办捏
passage_table = Table('PSG', metadata,
                    Column('PID', Integer(), primary_key=True),
                    Column('PTitle', String(255), nullable=False),
                    Column('PType', Boolean(), nullable=False, default=1),
                    Column('PUID', ForeignKey('USR.UID')),
                    Column('PAbstract', String(1024), nullable=False),
                    Column('PContent', Text(), nullable=False),
                    Column('PLink', String(1024)),
                    Column('PTag', String(255), index=True),
                    Column('PPermission', Integer(), nullable=False, default=0),
                    Column('PCNum', Integer(), nullable=False, default=0),
                    Column('PLikes', Integer(), nullable=False, default=0),
                    Column('PSubdate', DateTime(), default=datetime.now())
                    )

#评论表，CUID以UID作为外键
comment_table = Table('CMT', metadata,
                    Column('CID', Integer(), primary_key=True),
                    Column('CPID', ForeignKey('PSG.PID')),
                    Column('CUID', ForeignKey('USR.UID')),
                    Column('CContent', Text(), nullable=False),
                    Column('CLikes', Integer(), nullable=False, default=0),
                    Column('CSubdate', DateTime(), nullable=False, default=datetime.now())
                    )

#工具表，不知道具体要怎么实例化
tool_table = Table('TOL', metadata,
                    Column('TID', Integer(), primary_key=True),
                    Column('TTitle', String(255), nullable=False),
                    Column('TType', Boolean(), nullable=False),
                    Column('TUID', ForeignKey('USR.UID')),
                    Column('TAbstract', String(1024), nullable=False),
                    Column('TContent', Text(), nullable=False),
                    Column('TLink', String(1024), nullable=False),
                    Column('TTag', String(256), nullable=False, index=True),
                    Column('TPermission', Integer(), nullable=False)
                    )

# 在engine中新建以上表
if __name__ == "__main__":
    metadata.create_all(engine)
