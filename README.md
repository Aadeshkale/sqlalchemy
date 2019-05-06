Refrence sites :-
___________________

https://docs.sqlalchemy.org/en/13/orm/tutorial.html#adding-and-updating-objects
https://leportella.com/english/2019/01/10/sqlalchemy-basics-tutorial.html
___________________________________________________________________________________________________

Sqlalchemy :- 
	The SQLAlchemy Object Relational Mapper presents a method of associating user-defined Python classes with database tables, and instances of those classes (objects) with rows in their corresponding tables. It includes a system that transparently synchronizes all changes in state between objects and their related rows, called a unit of work, as well as a system for expressing database queries in terms of the user defined classes and their defined relationships between each other.
___________________________________________________________________________________________________

Installation :-
	pip3 install sqlalchemy
___________________________________________________________________________________________________

A.Creating tables in the database :- 
	1.import packages as follows

	from sqlalchemy import create_engine 		# used to create database connection
	from sqlalchemy import Column, String,Integer	# sqlalchemy types for table creation
	from sqlalchemy.ext.declarative import declarative_base # base class for table creation
	from sqlalchemy.orm import sessionmaker 	# session used to perform CRUD opration on
 							# database tables


	2.creating connection to perticular database
	
	engine = create_engine("sqlite:///mydb.db", echo=True) # connecting to mydb.db database
	session = sessionmaker(bind=engine)()		# session used to perform CRUD opration
	Base = declarative_base()			# base class initlization



	# creating table


	class Info(Base):

	    __tablename__ = "info"
	    id = Column(Integer,primary_key=True)
	    name = Column(String)

	    def __init__(self,id,name):
		self.id = id
		self.name = name

	Base.metadata.create_all(engine)  # required to first time for actually creating table 						  # into database
_____________________________________________________________________________________________________

B.Various oprations on database table

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

_____________________________________________________________________________________________________
	

