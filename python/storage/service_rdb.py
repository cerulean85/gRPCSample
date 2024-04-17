from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Text, TIMESTAMP, update
from sqlalchemy.orm import sessionmaker, declarative_base
import conf.service_config as service_conf

rdb_conf = service_conf.get_storage_conf(target="rdb")

rdb_conf_local = rdb_conf["app"]["local"]
rdb_conf_local_username = rdb_conf_local["username"]
rdb_conf_local_password = rdb_conf_local["password"]
rdb_conf_local_host = rdb_conf_local["host"]
rdb_conf_local_port = rdb_conf_local["port"]
rdb_conf_local_dbname = rdb_conf_local["dbname"]

rdb_conf_local_url  = f"postgresql://{rdb_conf_local_username}:"
rdb_conf_local_url += f"{rdb_conf_local_password}@{rdb_conf_local_host}:"
rdb_conf_local_url += f"{rdb_conf_local_port}/{rdb_conf_local_dbname}?"
rdb_conf_local_url += f"client_encoding=utf8"

engine = create_engine(rdb_conf_local_url)
Base = declarative_base()

class BotBoard(Base):
    __tablename__ = "botboard"
    idx = Column(Integer, primary_key=True)
    article_id = Column(Text)
    state = Column(Text)
    type = Column(Text)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

def get_rdb_session():
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    return session

def get_bot_board_record(count=50):
    session = get_rdb_session()
    record = session.query(BotBoard).limit(count).all()
    return record