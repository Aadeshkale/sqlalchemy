from sqlalchemy import create_engine
from sqlalchemy import Column, String,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///mydb.db", echo=True)
session = sessionmaker(bind=engine)()
Base = declarative_base()

# creating table


class Info(Base):

    __tablename__ = "info"
    id = Column(Integer,primary_key=True)
    name = Column(String)

    def __init__(self,id,name):
        self.id = id
        self.name = name

# Base.metadata.create_all(engine)  # required to first time for actually creating table into database

# adding data into table

info = Info(14,"kunal")
session.add(info)
session.commit()

# accessing all information from table

data = session.query(Info).all()
for i in data:
    print(i.id,'-->',i.name)

# accessing perticular information from table

data = session.query(Info).filter_by(name='aade').first()
print(data.id)

# another way accessing perticular information from table

data = session.query(Info).filter(Info.id==13).first()
print(data.name)


# update opration

ob = session.query(Info).filter_by(id=14).first()
print(ob.id,'-->',ob.name)
ob.name="aade"
session.commit()

# delete opration

ob = session.query(Info).filter_by(id=14).first()
session.delete(ob)
session.commit()

