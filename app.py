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
from flask_sqlalchemy import SQLAlchemy

#################################################
## Database Setup using SQLAlchemy
#################################################
## create a connection with the database
engine = create_engine("sqlite:///static/db/energyData.sqlite")
## reflect an existing database into a new model
Base = automap_base()
## reflect the tables
Base.prepare(engine, reflect=True)
# reflect all of the classes mapped to the Base
Base.classes.keys()
# create a "Metadata" Layer That Abstracts our SQL Database
Base.metadata.create_all(engine)
# Save a reference to the StateEnergyConumptionSector table as `ConsumptionSector`
ConsumptionSector = Base.classes.StateEnergyConsumptionSector
# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

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
        consumption_sector_dict["State"] = State
        consumption_sector_dict["Residential"] = Residential
        consumption_sector_dict["Commercial"] = Commercial
        consumption_sector_dict["Industrial"] = Industrial
        consumption_sector_dict["Transportation"] = Transportation
        consumption_sector.append(consumption_sector_dict)
    return jsonify(consumption_sector)
    
    
    
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
