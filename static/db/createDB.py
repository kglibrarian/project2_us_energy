##########################
## Import Libraries and Dependencies
##########################
import sqlite3, csv
import sqlite3
import pandas as pd
from numpy import genfromtxt
from time import time
from datetime import datetime
from sqlalchemy import Column, String, Integer, Float, Date, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

###################################
## How to use this file
###################################
## Run this file once to create the database from 
## the CSVs in the data file
## Open this file in the terminal and run: python createDB.py


####################################
## Function to Load the Database file
####################################

def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    return data.tolist()

##################################
## SQLAlchemy Declarative base
# ################################
# The declarative base is a function that returns 
# a new base class from which all mapped classes 
# should inherit.

Base = declarative_base()

##################################
## Create Classes 
##################################
#Create a class that describes each table in the database

class StateEnergyConsumptionSector(Base):
    __tablename__ = 'StateEnergyConsumptionSector'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    State = Column(VARCHAR(40))
    Residential = Column(Integer)
    Commercial = Column(Integer)
    Industrial = Column(Integer)
    Transportation = Column(Integer)
    
####################################
## SQLAlchemy to Load CSV data into Tables
####################################
#Within the if statement that will create the database using 
# the classes that have already been described (see above)

if __name__ == "__main__":
    t = time()

    #Create the database
    engine = create_engine('sqlite:///energyData.sqlite')
    Base.metadata.create_all(engine)
    
    # Query All Records in the the Database
    data = engine.execute("SELECT * FROM StateEnergyConsumptionSector")
    for record in data:
        print(record)

    #Create the session
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    try:
        file_name = "../data/Energy_Consumption_by_Sector_2017.csv" #sample CSV file used:  http://www.google.com/finance/historical?q=NYSE%3AT&ei=W4ikVam8LYWjmAGjhoHACw&output=csv
        data = Load_Data(file_name) 

        for i in data:
            record = StateEnergyConsumptionSector(**{
                'State' : i[0],
                'Residential' : i[1],
                'Commercial' : i[2],
                'Industrial' : i[3],
                'Transportation' : i[4],
                
            })
            s.add(record) #Add all the records

        s.commit() #Attemto commit all the records
        
        
    except:
        s.rollback() #Rollback the changes on error
    finally:
        s.close() #Close the connection
        #print "Time elapsed: " + str(time() - t) + " s." #0.091s

## This code is modified from: #https://stackoverflow.com/questions/31394998/using-sqlalchemy-to-load-csv-file-into-a-database

#############################
## Creating a Database using Pandas to_SQL function
#############################

# # # load data
# df = pd.read_csv('../data/Energy_Consumption_by_Sector_2017.csv')
# df2 = pd.read_csv('../data/Electricity_Generation_by_Source_Feb._2019.csv')

# # # strip whitespace from headers
# df.columns = df.columns.str.strip()
# df2.columns = df2.columns.str.strip()
# con = sqlite3.connect("energyData.sqlite")

# # # drop data into database
# df.to_sql("energyconsumpsector", con)
# df2.to_sql("electricitygeneration", con)

# # # create a primary key for each table
# con.execute('alter table energyconsumpsector add primary key(id)')
# con.execute('alter table electricitygeneration add primary key(id)')
# con.close()

###############################
## Interact with a SQLite database in terminal
###############################
## Open the energydata.db in the terminal 
## Use these commands: 
## sqlite3 energyData.sqlite
## .tables   ## prints a list of the tables in the db
## .dump     ## prints the data in the database
## .exit     ## to exit the db file
