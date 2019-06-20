import sqlite3, csv
import sqlite3
import pandas as pd

# load data
df = pd.read_csv('../data/Energy_Consumption_by_Sector_2017.csv')
df2 = pd.read_csv('../data/Electricity_Generation_by_Source_Feb._2019.csv')
# # strip whitespace from headers
df.columns = df.columns.str.strip()
df2.columns = df2.columns.str.strip()
con = sqlite3.connect("energyData.sqlite")

# # drop data into database
df.to_sql("energyconsumpsector", con)
df2.to_sql("electricitygeneration", con)

# # create a primary key for each table
con.execute('alter table energyconsumpsector add primary key(id)')
con.execute('alter table electricitygeneration add primary key(id)')
con.close()

#to test this, open the energydata.db in the terminal 
#and use these commands: 
# sqlite3 energydata.db
#.tables ##shows you a list of the tables in the db
#.dump ##
#.exit ##let's you exit the db file
#https://stackoverflow.com/questions/31394998/using-sqlalchemy-to-load-csv-file-into-a-database
#https://stackoverflow.com/questions/31394998/using-sqlalchemy-to-load-csv-file-into-a-database

# from numpy import genfromtxt
# from time import time
# from datetime import datetime
# from sqlalchemy import Column, String, Integer, Float, Date, VARCHAR
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# def Load_Data(file_name):
#     data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
#     return data.tolist()

# Base = declarative_base()

# class StateEnergyConsumptionSector(Base):
#     __tablename__ = 'StateEnergyConsumptionSector'
#     __table_args__ = {'sqlite_autoincrement': False}
#     id = Column(Integer, primary_key=True, nullable=False)
#     State = Column(VARCHAR(40))
#     Residential = Column(Integer)
#     Commercial = Column(Integer)
#     Industrial = Column(Integer)
#     Transportation = Column(Integer)
    

# if __name__ == "__main__":
#     t = time()

#     #Create the database
#     engine = create_engine('sqlite:///energyData.sqlite')
#     Base.metadata.create_all(engine)

#     #Create the session
#     session = sessionmaker()
#     session.configure(bind=engine)
#     s = session()

#     try:
#         file_name = "../data/Energy_Consumption_by_Sector_2017.csv" #sample CSV file used:  http://www.google.com/finance/historical?q=NYSE%3AT&ei=W4ikVam8LYWjmAGjhoHACw&output=csv
#         data = Load_Data(file_name) 

#         for i in data:
#             record = StateEnergyConsumptionSector(**{
#                 'State' : i[0],
#                 'Residential' : i[1],
#                 'Commercial' : i[2],
#                 'Industrial' : i[3],
#                 'Transportation' : i[4],
                
#             })
#             s.add(record) #Add all the records

#         s.commit() #Attemto commit all the records
#     except:
#         s.rollback() #Rollback the changes on error
#     finally:
#         s.close() #Close the connection
#         #print "Time elapsed: " + str(time() - t) + " s." #0.091s