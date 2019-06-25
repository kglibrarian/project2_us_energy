# import necessary libraries
import sqlite3
import json
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

#################################################
## Database Setup using SQLAlchemy
#################################################
## create a connection with the database
engine = create_engine("sqlite:///static/db/energyData.sqlite", connect_args={'check_same_thread': False})
## reflect an existing database into a new model
Base = automap_base()
## reflect the tables
Base.prepare(engine, reflect=True)
# reflect all of the classes mapped to the Base
Base.classes.keys()
# create a "Metadata" Layer That Abstracts our SQL Database
Base.metadata.create_all(engine)
# Save a reference to the StateEnergyConumptionSector table as `ConsumptionSector`
ConsumptionSector = Base.classes.energy_consumption_sector
ElectricityGeneration = Base.classes.electricity_generation_source
EnergyConsumption = Base.classes.energy_consumption_estimates
PlantData = Base.classes.plant_data
EnergyProduction = Base.classes.energy_production
# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
CORS(app)

#################################################
# Flask Routes
#################################################

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/mina")
def mina():
    return render_template("mina.html")

@app.route("/kentucky")
def kentucky():
    return render_template("kentucky.html")

@app.route("/api/v1.0/consumptionsector")

def consumptionSectors():
    # Query all states
    results = session.query(ConsumptionSector.State, 
            ConsumptionSector.Residential, 
            ConsumptionSector.Commercial, 
            ConsumptionSector.Industrial,
            ConsumptionSector.Transportation).all()
    #print(results)
    # Create a dictionary from the row data and append to a list of all_passengers
    consumption_sector = []
    for State, Residential, Commercial, Industrial, Transportation in results:
        consumption_sector_dict = {}
    #    consumption_sector_dict["State"] = State
        consumption_sector_dict["Residential"] = Residential
        consumption_sector_dict["Commercial"] = Commercial
        consumption_sector_dict["Industrial"] = Industrial
        consumption_sector_dict["Transportation"] = Transportation
        consumption_sector.append(consumption_sector_dict)
    return jsonify(consumption_sector)
    

@app.route("/api/v1.0/electricityGeneration")

def electricityGeneration():
    # Query all states
    results = session.query(ElectricityGeneration.State, 
            ElectricityGeneration.Petroleum_Fired, 
            ElectricityGeneration.Natural_Gas_Fired, 
            ElectricityGeneration.Coal_Fired,
            ElectricityGeneration.Nuclear,
            ElectricityGeneration.Hydroelectric,
            ElectricityGeneration.Nonhydroelectric_Renewables).all()
    #print(results)
    # Create a dictionary from the row data and append to a list of all_passengers
    electricity_generation = []
    for State, Petroleum_Fired, Natural_Gas_Fired, Coal_Fired, Nuclear, Hydroelectric, Nonhydroelectric_Renewables  in results:
        electricity_generation_dict = {}
        electricity_generation_dict["State"] = State
        electricity_generation_dict["Petroleum Fired"] = Petroleum_Fired
        electricity_generation_dict["Natural Gas Fired"] = Natural_Gas_Fired
        electricity_generation_dict["Coal Fired"] = Coal_Fired
        electricity_generation_dict["Nuclear"] = Nuclear
        electricity_generation_dict["Hydroelectric"] = Hydroelectric
        electricity_generation_dict["Nonhydroelectric_Renewables"] = Nonhydroelectric_Renewables
        electricity_generation.append(electricity_generation_dict)
    return jsonify(electricity_generation)

@app.route("/api/v1.0/energyConsumption")
def energyConsumption():
    # Query all states
    results = session.query(EnergyConsumption.State, 
            EnergyConsumption.Coal, 
            EnergyConsumption.Natural_Gas, 
            EnergyConsumption.Motor_Gasoline_excl_Ethanol,
            EnergyConsumption.Distillate_Fuel_Oil,
            EnergyConsumption.Jet_Fuel,
            EnergyConsumption.HGL,
            EnergyConsumption.Residual_Fuel,
            EnergyConsumption.Other_Petroleum,
            EnergyConsumption.Nuclear_Electric_Power,
            EnergyConsumption.Hydroelectric_Power,
            EnergyConsumption.Biomass,
            EnergyConsumption.Other_Renewables,
            EnergyConsumption.Net_Electricity_Imports,
            EnergyConsumption.Net_Interstate_Flow_of_Electricity).all()
    #print(results)
    # Create a dictionary from the row data and append to a list of all_passengers
    energy_consumption = []
    
    for State, Coal, Natural_Gas, Motor_Gasoline_excl_Ethanol, Distillate_Fuel_Oil, Jet_Fuel, HGL, Residual_Fuel, Other_Petroleum, Nuclear_Electric_Power, Hydroelectric_Power, Biomass, Other_Renewables, Net_Electricity_Imports, Net_Interstate_Flow_of_Electricity in results:
        energy_consumption_dict = {}
        energy_consumption_dict["State"] = State
        energy_consumption_dict["Coal"] = Coal
        energy_consumption_dict["Natural_Gas"] = Natural_Gas
        energy_consumption_dict["Motor_Gasoline_excl_Ethanol"] = Motor_Gasoline_excl_Ethanol
        energy_consumption_dict["Distillate_Fuel_Oil"] = Distillate_Fuel_Oil
        energy_consumption_dict["Jet_Fuel"] = Jet_Fuel
        energy_consumption_dict["HGL"] = HGL
        energy_consumption_dict["Residual_Fuel"] = Residual_Fuel
        energy_consumption_dict["Other_Petroleum"] = Other_Petroleum
        energy_consumption_dict["Nuclear_Electric_Power"] = Nuclear_Electric_Power
        energy_consumption_dict["Hydroelectric_Power"] = Hydroelectric_Power
        energy_consumption_dict["Biomass"] = Biomass
        energy_consumption_dict["Other_Renewables"] = Other_Renewables
        energy_consumption_dict["Net_Electricity_Imports"] = Net_Electricity_Imports
        energy_consumption_dict["Net_Interstate_Flow_of_Electricity"] = Net_Interstate_Flow_of_Electricity
        energy_consumption.append(energy_consumption_dict)
    #print(energy_consumption)
    return jsonify(energy_consumption)

@app.route("/api/v1.0/plantData")
def plantData():
    # Query all states
    results = session.query(PlantData.Utility_ID, 
            PlantData.Utility_Name, 
            PlantData.Plant_Code, 
            PlantData.Plant_Name, 
            PlantData.Street_Address, 
            PlantData.City, 
            PlantData.State, 
            PlantData.Zip, 
            PlantData.County, 
            PlantData.Latitude, 
            PlantData.Longitude, 
            PlantData.Name_of_Water_Source, 
            PlantData.Primary_Purpose_NAICS_Code, 
            PlantData.Sector_Name,
            PlantData.Grid_Voltage_kV).all()
    #print(results)
  
    # Create a dictionary from the row data and append to a list of all_passengers
       
    plant_data = []
   
    for Utility_ID, Utility_Name, Plant_Code, Plant_Name, Street_Address, City, State, Zip, County, Latitude, Longitude, Name_of_Water_Source, Primary_Purpose_NAICS_Code, Sector_Name, Grid_Voltage_kV in results:
        plant_data_dict = {}
        plant_data_dict["Utility_ID"] = Utility_ID
        plant_data_dict["Utility_Name"] = Utility_Name
        plant_data_dict["Plant_Name"] = Plant_Name
        plant_data_dict["Street_Address"] = Street_Address
        plant_data_dict["City"] = City
        plant_data_dict["State"] = State
        plant_data_dict["Zip"] = Zip
        plant_data_dict["County"] = County
        plant_data_dict["Latitude"] = Latitude
        plant_data_dict["Longitude"] = Longitude
        plant_data_dict["Name_of_Water_Source"] = Name_of_Water_Source
        plant_data_dict["Primary_Purpose_NAICS_Code"] = Primary_Purpose_NAICS_Code
        plant_data_dict["Sector_Name"] = Sector_Name
        plant_data_dict["Grid_Voltage_kV"] = Grid_Voltage_kV
        plant_data.append(plant_data_dict)
    #print(plant_data[1])
    return jsonify(plant_data)

@app.route("/api/v1.0/energyProduction")
def energyProduction():
    # Query all states
    results = session.query(EnergyProduction.State, 
            EnergyProduction.Coal, 
            EnergyProduction.Natural_Gas_Marketed, 
            EnergyProduction.Crude_Oil, 
            EnergyProduction.Nuclear_Electric_Power, 
            EnergyProduction.Biofuels, 
            EnergyProduction.Other_Renewable_Energy).all()
    #print(results)

    # Create a dictionary from the row data and append to a list of all_passengers
       
    energy_production = []
   
    for State, Coal, Natural_Gas_Marketed, Crude_Oil, Nuclear_Electric_Power, Biofuels, Other_Renewable_Energy in results:
        energy_production_dict = {}
        energy_production_dict["State"] = State
        energy_production_dict["Coal"] = Coal
        energy_production_dict["Natural_Gas_Marketed"] = Natural_Gas_Marketed
        energy_production_dict["Crude_Oil"] = Crude_Oil
        energy_production_dict["Nuclear_Electric_Power"] = Nuclear_Electric_Power
        energy_production_dict["Biofuels"] = Biofuels
        energy_production_dict["Other_Renewable_Energy"] = Other_Renewable_Energy
        energy_production.append(energy_production_dict)
    #print(energy_production)
    return jsonify(energy_production)





    ####################################
    ## Connect to database using sqlite3
    ###################################
    # con = sqlite3.connect('./assets/db/energyData.sqlite')
    # c = con.cursor()
    # result = c.execute('select * from energyconsumpsector')
    # items = [dict(zip([key[0] for key in c.description],row))for row in result]
    # print(json.dumps({'EnergyConsumptionSector':items}))
    # response = jsonify(items)
    # con.close()
    #return response

if __name__ == "__main__":
    app.run()
