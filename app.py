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
# Database Setup
#################################################
#engine = create_engine("sqlite:///assets/db/energyData.sqlite")

# reflect an existing database into a new model
#Base = automap_base()
# reflect the tables
#Base.prepare(engine, reflect=True)

# Save reference to the table
#consumption = Base.classes.energyconsumpsector

# Create our session (link) from Python to the DB
#session = Session(engine)




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

@app.route("/api/v1.0/states")
def names():
    con = sqlite3.connect('./assets/db/energyData.sqlite')
    c = con.cursor()
    result = c.execute('select * from energyconsumpsector')
    items = [dict(zip([key[0] for key in c.description],row))for row in result]
    print(json.dumps({'EnergyConsumptionSector':items}))
    response = jsonify(items)
    con.close()
    
    
    return response

if __name__ == "__main__":
    app.run()
