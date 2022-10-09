
import datetime as dt
import numpy as mp
import pandas as pd




import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func




from flask import Flask, jsonify




engine = create_engine("sqlite:///hawaii.sqlite")




Base = automap_base()




Base.prepare(engine, reflect=True)




Measurement = Base.classes.measurement
Station = Base.classes.station




session = Session(engine)




app = Flask(__name__)




@app.route("/")
def welcome():
   return(
   
   f"Welcome to the Climate Analysis API! <br/>"
   f"Available Routes: <br/>"
   f"/api/v1.0/precipitation <br/>"
   f"/api/v1.0/stations <br/>"
   f"/api/v1.0/tobs <br/>"
   f"/api/v1.0/temp/start/end <br/>"
   )


