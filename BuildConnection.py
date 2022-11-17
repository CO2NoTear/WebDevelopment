from sqlalchemy import create_engine
# 连接到本地SQL服务器with mysql+pymysql方言
engine = create_engine("mysql+pymysql://root:admin@localhost/alchemy_test", pool_recycle=3600)
connection = engine.connect()

if __name__ == "__main__":
    engine.connect()
