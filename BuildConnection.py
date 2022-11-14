from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:admin@localhost/alchemy_test", pool_recycle=3600)
connection = engine.connect()

if __name__ == "__main__":
    engine.connect()