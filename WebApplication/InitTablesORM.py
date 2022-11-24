from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import \
        Integer, String, Text, Boolean, \
        DateTime, Column, MetaData, ForeignKey, \
        Table, Numeric
from BuildConnection import engine
from sqlalchemy.ext.declarative import declarative_base 

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

#用户表，主键：UID
#无外键。 UID作为其他表的重要外键。
#UName 添加了索引
class User(Base):
    __tablename__ = 'USR'

    UID = Column(Integer(), primary_key=True)
    UName = Column(String(64), nullable=False, unique=True, index=True)
    UPassword = Column(String(256), nullable=False)
    UMoto = Column(String(256), nullable=False, default='Lazy guy with nothing left here.')
    ULevel = Column(Integer(), nullable=False, default=1)
    UExp = Column(Integer(), nullable=False,default=0)
    UType = Column(Integer(), nullable=False, default=0)
    UIntro = Column(Text(), nullable=False)
    UPNum = Column(Integer(),default=0,nullable=False)

    def __repr__(self):
        return "User(UID={self.UID}, "\
                "UName={self.UName},"\
                "UPassword={self.UPassword},"\
                "UMoto={self.UMoto},"\
                "ULevel={self.ULevel},"\
                "UExp={self.UExp},"\
                "UType={self.UType},"\
                "UIntro={self.UIntro},"\
                "UPNum={self.UPNum})".format(self=self)

# 文章表，PUID以UID作为外键
# 不知道PLink要怎么办捏
class Passage(Base):
    __tablename__ = 'PSG'

    PID = Column(Integer(), primary_key=True)
    PTitle = Column(String(255), nullable=False)
    PType = Column(Boolean(), nullable=False, default=1)
    PUID = Column(ForeignKey('USR.UID'))
    PAbstract = Column(String(1024), nullable=False)
    PContent = Column(Text(), nullable=False)
    PLink = Column(String(1024))
    PTag = Column(String(255), index=True)
    PPermission = Column(Integer(), nullable=False, default=0)
    PCNum = Column(Integer(), nullable=False, default=0)
    PLikes = Column(Integer(), nullable=False, default=0)
    PSubdate = Column(DateTime(), default=datetime.now())


#评论表，CUID以UID作为外键
class Comment(Base):
    __tablename__ = 'CMT'
    CID = Column(Integer(), primary_key=True)
    CPID = Column(ForeignKey('PSG.PID'))
    CUID = Column(ForeignKey('USR.UID'))
    CContent = Column(Text(), nullable=False)
    CLikes = Column(Integer(), nullable=False, default=0)
    CSubdate = Column(DateTime(), nullable=False, default=datetime.now())

#工具表，不知道具体要怎么实例化
class Tool(Base):
    __tablename__ = 'TOL'
    TID = Column(Integer(), primary_key=True)
    TTitle = Column(String(255), nullable=False)
    TType = Column(Boolean(), nullable=False)
    TUID = Column(ForeignKey('USR.UID'))
    TAbstract = Column(String(1024), nullable=False)
    TContent = Column(Text(), nullable=False)
    TLink = Column(String(1024), nullable=False)
    TTag = Column(String(256), nullable=False, index=True)
    TPermission = Column(Integer(), nullable=False)
        

# 在engine中新建以上表
if __name__ == "__main__":
    Base.metadata.create_all(engine)
