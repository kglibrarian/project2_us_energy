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
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import *
from datetime import datetime, timedelta
from random import randint
import os
import csv
import datetime
import sys
import numpy as np
from io import StringIO
###################################
## How to use this file
###################################
## Run this file once to create the database from 
## the CSVs in the data file
## Open this file in the terminal and run: python createDB.py




##################################
## SQLAlchemy Declarative base
# ################################
# The declarative base is a function that returns 
# a new base class from which all mapped classes 
# should inherit.

#Create the database
engine = create_engine('sqlite:///energyData.sqlite')
Base = declarative_base()

#https://www.freecodecamp.org/news/sqlalchemy-makes-etl-magically-easy-ab2bd0df928/

##################################
## Define Schema (i.e. Create Classes)
##################################
#Create a class that describes each table in the database

class Energy_consumption_sector(Base):
    __tablename__ = 'energy_consumption_sector'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    State = Column(VARCHAR(40))
    Residential = Column(Integer)
    Commercial = Column(Integer)
    Industrial = Column(Integer)
    Transportation = Column(Integer)

class Electricity_generation_source(Base):
    __tablename__ = 'electricity_generation_source'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    State = Column(VARCHAR(40))
    Petroleum_Fired = Column(Integer)
    Natural_Gas_Fired = Column(Integer)
    Coal_Fired = Column(Integer)
    Nuclear = Column(Integer)
    Hydroelectric = Column(Integer)
    Nonhydroelectric_Renewables = Column(Integer)
    		
class Energy_consumption_estimates(Base):
    __tablename__ = 'energy_consumption_estimates'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    State = Column(VARCHAR(40))
    Coal = Column(Integer)
    Natural_Gas = Column(Integer)
    Motor_Gasoline_excl_Ethanol = Column(Integer)
    Distillate_Fuel_Oil = Column(Integer)
    Jet_Fuel = Column(Integer)
    HGL = Column(Integer)
    Residual_Fuel = Column(Integer)
    Other_Petroleum = Column(Integer)
    Nuclear_Electric_Power = Column(Integer)
    Hydroelectric_Power = Column(Integer)
    Biomass = Column(Integer)
    Other_Renewables = Column(Integer)
    Net_Electricity_Imports = Column(Integer)
    Net_Interstate_Flow_of_Electricity = Column(Integer)
       
class Plant_data(Base):
    __tablename__ = 'plant_data'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    Utility_ID = Column(Integer)
    Utility_Name = Column(VARCHAR(40))
    Plant_Code = Column(Integer)
    Plant_Name = Column(VARCHAR(40))
    Street_Address = Column(VARCHAR(40))
    City = Column(VARCHAR(40))
    State = Column(VARCHAR(40))
    Zip = Column(Integer)
    County = Column(VARCHAR(40))
    Latitude = Column(Integer)
    Longitude = Column(Integer)
    Name_of_Water_Source = Column(VARCHAR(40))
    Primary_Purpose_NAICS_Code = Column(Integer)
    Sector_Name = Column(Integer)
    Grid_Voltage_kV = Column(Integer)

class Energy_production(Base):
    __tablename__ = 'energy_production'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    State = Column(VARCHAR(40))
    Coal = Column(Integer)
    Natural_Gas_Marketed = Column(Integer)
    Crude_Oil = Column(Integer)
    Nuclear_Electric_Power = Column(Integer)
    Biofuels = Column(Integer)
    Other_Renewable_Energy = Column(Integer)

Energy_consumption_sector.__table__.create(bind=engine, checkfirst=True)
Electricity_generation_source.__table__.create(bind=engine, checkfirst=True)
Energy_consumption_estimates.__table__.create(bind=engine, checkfirst=True)
Plant_data.__table__.create(bind=engine, checkfirst=True)
Energy_production.__table__.create(bind=engine, checkfirst=True)   

####################################
## Extract: Use SQLAlchemy to Load CSV data into Tables
####################################
#Within the if statement that will create the database using 
# the classes that have already been described (see above)
 
 
def load_1():
    #energy_consumption_sector_data = genfromtxt("../data/Energy_Consumption_by_Sector_2017.csv", delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    #print(energy_consumption_sector_data)
    #return energy_consumption_sector_data.tolist()
    energy_consumption_sector_data = pd.read_csv("../data/Energy_Consumption_by_Sector_2017.csv")
    energy_consumption_sector_data_list = energy_consumption_sector_data.values.tolist()
    #print(energy_consumption_sector_data_list)
    return energy_consumption_sector_data_list

#Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

try:
    data = load_1()
    #print(data)
    for i in data:
        
        record = Energy_consumption_sector(**{
                    'State' : i[0],
                    'Residential' : i[1],
                    'Commercial' : i[2],
                    'Industrial' : i[3],
                    'Transportation' : i[4]
                        })
        #print(record)
        s.add(record) #Add all the records

    s.commit() #Attempt to commit all the records   
#http://docs.pyexcel.org/en/latest/showcases/db_injection.html
except:
    s.rollback() #Rollback the changes on error
finally:
    s.close() #Close the connection
#print("Time elapsed: " + str(time() - t) + " s.") #0.091s

####################################
## Extract: Use SQLAlchemy to Load CSV data into Tables
####################################


def load_2():
    #electricity_generation_source = genfromtxt("C:/Users/keg827/Documents/3 Data Science Bootcamp Code/project2_us_energy/static/data/Electricity_Generation_by_Source_2019.csv", delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    #print(electricity_generation_source)
    #return electricity_generation_source.tolist() 
    electricity_generation_source = pd.read_csv("C:/Users/keg827/Documents/3 Data Science Bootcamp Code/project2_us_energy/static/data/Electricity_Generation_by_Source_2019.csv") 
    electricity_generation_source_list = electricity_generation_source.values.tolist()
    #print(electricity_generation_source_list)
    return electricity_generation_source_list

#Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

try:
    data_2 = load_2()
    #print(data_2)
    for i in data_2:
        print(i)
        record = Electricity_generation_source(**{
                    'State' : i[0],
                    'Petroleum_Fired' : i[1],
                    'Natural_Gas_Fired' : i[2],
                    'Coal_Fired' : i[3],
                    'Nuclear' : i[4],
                    'Hydroelectric': i[5],
                    'Nonhydroelectric_Renewables': i[6]
                        })
        #print(record)
        s.add(record) #Add all the records

    s.commit() #Attempt to commit all the records   
#http://docs.pyexcel.org/en/latest/showcases/db_injection.html
except:
    s.rollback() #Rollback the changes on error
finally:
    s.close() #Close the connection
#print("Time elapsed: " + str(time() - t) + " s.") #0.091s

def load_3():
    #energy_consumption_estimates = genfromtxt("C:/Users/keg827/Documents/3 Data Science Bootcamp Code/project2_us_energy/static/data/Energy_Consumption_Estimates_2017.csv", delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    #print(energy_consumption_estimates)
    #return energy_consumption_estimates.tolist() 
    energy_consumption_estimates = pd.read_csv("C:/Users/keg827/Documents/3 Data Science Bootcamp Code/project2_us_energy/static/data/Energy_Consumption_Estimates_2017.csv")
    energy_consumption_estimates_list = energy_consumption_estimates.values.tolist()
    #print(energy_consumption_estimates_list)
    return energy_consumption_estimates_list

#Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

try:
    data_3 = load_3()
    #print(data_3)
    for a in data_3:
        #print(a)
        
        record_3 = Energy_consumption_estimates(**{
                    'State' : a[0],
                    'Coal' : a[1],
                    'Natural_Gas' : a[2],
                    'Motor_Gasoline_excl_Ethanol' : a[3],
                    'Distillate_Fuel_Oil' : a[4],
                    'Jet_Fuel': a[5],
                    'HGL': a[6],
                    'Residual_Fuel': a[7],
                    'Other_Petroleum': a[8],
                    'Nuclear_Electric_Power': a[9],
                    'Hydroelectric_Power': a[10],
                    'Biomass': a[11],
                    'Other_Renewables': a[12],
                    'Net_Electricity_Imports': a[13],
                    'Net_Interstate_Flow_of_Electricity': a[14]
                        })
        #print(record_3)
        s.add(record_3) #Add all the records
    
    s.commit() #Attempt to commit all the records   
#http://docs.pyexcel.org/en/latest/showcases/db_injection.html
except:
     s.rollback() #Rollback the changes on error
     print("there was an error")
finally:
     s.close() #Close the connection
     print("session is closed")
#print("Time elapsed: " + str(time() - t) + " s.") #0.091s


def load_4():
    #plant_data = np.genfromtxt("C:/Users/keg827/Documents/3 Data Science Bootcamp Code/project2_us_energy/static/data/Plant_Y2017_Final_Data.csv",delimiter=',', autostrip=True, skip_header=1, usecols=np.arange(0,15), invalid_raise = False, deletechars="~!@#$%^&*()-=+~\|]}[{';: /?.>,<.", dtype='unicode', converters={0: lambda s: str(s)})
    #print(plant_data)
    #return plant_data.tolist()
    plant_data = pd.read_csv("C:/Users/keg827/Documents/3 Data Science Bootcamp Code/project2_us_energy/static/data/Plant_Y2017_Final_Data.csv")
    plant_data_list = plant_data.values.tolist()
    #print(plant_data_list)
    return plant_data_list

#Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

try:
    data_4 = load_4()
    #print(data_4)
    for i in data_4:
        #print(i)
        record_4 = Plant_data(**{
                    'Utility_ID' : i[0],
                    'Utility_Name' : i[1],
                    'Plant_Code' : i[2],
                    'Plant_Name' : i[3],
                    'Street_Address' : i[4],
                    'City' : i[5],
                    'State' : i[6],
                    'Zip' : i[7],
                    'County' : i[8],
                    'Latitude' : i[9],
                    'Longitude' : i[10],
                    'Name_of_Water_Source' : i[11],
                    'Primary_Purpose_NAICS_Code' : i[12],
                    'Sector_Name' : i[13],
                    'Grid_Voltage_kV' : i[14]
                     })
        #print(record_4)
        s.add(record_4) #Add all the records
    
    s.commit() #Attempt to commit all the records   



except:
    s.rollback() #Rollback the changes on error
    print("there was an error")
finally:
    s.close() #Close the connection
    print("session is closed")       


def load_5():
    #energy_production = np.genfromtxt("C:/Users/keg827/Documents/3 Data Science Bootcamp Code/project2_us_energy/static/data/Energy_Production_Estimates.csv",delimiter=',', autostrip=True, skip_header=1, usecols=np.arange(0,15), invalid_raise = False, deletechars="~!@#$%^&*()-=+~\|]}[{';: /?.>,<.", dtype='unicode', converters={0: lambda s: str(s)})
    #print(energy_production)
    #return energy_production.tolist()
    energy_production = pd.read_csv("C:/Users/keg827/Documents/3 Data Science Bootcamp Code/project2_us_energy/static/data/Energy_Production_Estimates.csv")
    energy_production_list = energy_production.values.tolist()
    #print(plant_data_list)
    return energy_production_list

#Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

try:
    data_5 = load_5()
    #print(data_5)
    for i in data_5:
        #print(i)
        record_5 = Energy_production(**{
                    'State' : i[0],
                    'Coal' : i[1],
                    'Natural_Gas_Marketed' : i[2],
                    'Crude_Oil' : i[3],
                    'Nuclear_Electric_Power' : i[4],
                    'Biofuels' : i[5],
                    'Other_Renewable_Energy' : i[6],
                    })
        #print(record_5)
        s.add(record_5) #Add all the records
    
    s.commit() #Attempt to commit all the records   



except:
    s.rollback() #Rollback the changes on error
    print("there was an error")
finally:
    s.close() #Close the connection
    print("session is closed")


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


######################################
## THE CODE BELOW WORKS FOR ONE CSV ##
######################################


####################################
## Function to Load the Database file
####################################

# def Load_Data(file_name):
#     data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
#     return data.tolist()

##################################
## SQLAlchemy Declarative base
# ################################
# The declarative base is a function that returns 
# a new base class from which all mapped classes 
# should inherit.

#Base = declarative_base()

##################################
## Create Classes 
##################################
#Create a class that describes each table in the database

# class StateEnergyConsumptionSector(Base):
#     __tablename__ = 'StateEnergyConsumptionSector'
#     __table_args__ = {'sqlite_autoincrement': True}
#     id = Column(Integer, primary_key=True, nullable=False)
#     State = Column(VARCHAR(40))
#     Residential = Column(Integer)
#     Commercial = Column(Integer)
#     Industrial = Column(Integer)
#     Transportation = Column(Integer)

#####################################
## SQLAlchemy to Load CSV data into Tables
####################################
#Within the if statement that will create the database using 
# the classes that have already been described (see above)

# if __name__ == "__main__":
#     t = time()

#     #Create the database
#     engine = create_engine('sqlite:///energyData.sqlite')
#     Base.metadata.create_all(engine)
    
#     # Query All Records in the the Database
#     data = engine.execute("SELECT * FROM StateEnergyConsumptionSector")
#     for record in data:
#         print(record)

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

## This code is modified from: #https://stackoverflow.com/questions/31394998/using-sqlalchemy-to-load-csv-file-into-a-database