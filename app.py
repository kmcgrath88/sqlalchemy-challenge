#################################################
#-----CLIMATE APP-----#
#################################################
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import datetime as dt

from flask import Flask, jsonify


#################################################
#-----Database Setup-----#
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#Reflect an existing database into a new model
Base = automap_base()
#Reflect the tables
Base.prepare(engine, reflect=True)

#Save reference to the table
#Hawaii = Base.classes.hawaii
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
session = Session(engine)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date<br/>"
        f"/api/v1.0/start_date/end_date<br/>"
    )

@app.route('/api/v1.0/precipitation')
def precipitation():
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    year = most_recent_date[0].split('-')
    last_12months = dt.date(int(year[0]), int(year[1]), int(year[2])) -  dt.timedelta(days = 365)
    # Perform a query to retrieve the data and precipitation scores
    pre = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= last_12months).all()

    pre_dict = {date: p for date, p in pre}
    return jsonify(pre_dict)

@app.route('/api/v1.0/stations')
def station():
    stations = session.query(Station.station).all()
    all_stations = list(np.ravel(stations))
    return jsonify(all_stations)

@app.route('/api/v1.0/tobs')
def tobs():
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    year = most_recent_date[0].split('-')
    last_12months = dt.date(int(year[0]), int(year[1]), int(year[2])) -  dt.timedelta(days = 365)

    last_year_temp = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= last_12months).all()
   
    temps= list(np.ravel(last_year_temp))
    
    return jsonify(temps)

@app.route('/api/v1.0/<start_date>')
def calc_temps(start_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    start = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()
    start_rav = list(np.ravel(start))

    return jsonify(start_rav)
    
@app.route('/api/v1.0/<start_date>/<end_date>')
def calc_temps2(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    start_end = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    start_end_rav = list(np.ravel(start_end))

    return jsonify(start_end_rav)

if __name__ == '__main__':
    app.run(debug=True)



