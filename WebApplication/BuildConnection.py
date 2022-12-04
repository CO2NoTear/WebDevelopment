from sqlalchemy import create_engine
# 连接到本地SQL服务器with mysql+pymysql方言
SQL_URI = r"mysql+pymysql://root:admin@localhost:3306/alchemy_test"
engine = create_engine(SQL_URI, pool_recycle=3600)
connection = engine.connect()

if __name__ == "__main__":
    engine.connect()
