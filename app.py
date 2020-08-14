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
engine = create_engine("sqlite:///Resources/hawaii.sqlite?check_same_thread=False")

#Reflect an existing database into a new model
Base = automap_base()
#Reflect the tables
Base.prepare(engine, reflect=True)

#Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
#-----Flask Setup-----#
app = Flask(__name__)

#################################################
#-----Flask Routes-----#
session = Session(engine)

#################################################
#Home page. List all routes that are available
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"<b>Available Routes:</b><br/>"
        f"<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"<br/>"
        f"/api/v1.0/stations<br/>"
        f"<br/>"
        f"/api/v1.0/tobs<br/>"
        f"<br/>"
        f"/api/v1.0/start_date<br/>"
        f"<i><b>Example:</b> /api/v1.0/2016-03-10</i><br/>"
        f"<br/>"
        f"/api/v1.0/start_date/end_date<br/>"
        f"<i><b>Example:</b> /api/v1.0/2016-03-10/2016-03-20</i>"
    )

#################################################
#Convert the query results to a dictionary using date as the key and prcp as the value. Return the 
#JSON representation of your dictionary.
@app.route('/api/v1.0/precipitation')
def precipitation():
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    year = most_recent_date[0].split('-')
    last_12months = dt.date(int(year[0]), int(year[1]), int(year[2])) - dt.timedelta(days = 365)
    pre = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= last_12months).all()

    pre_dict = {date: p for date, p in pre}
   
    return jsonify(pre_dict)

#################################################
#Return a JSON list of stations from the dataset.
@app.route('/api/v1.0/stations')
def station():
    stat = session.query(Station.station).all()
    all_stations = list(np.ravel(stat))
    return jsonify(all_stations)

#################################################
#Query the dates and temperature observations of the most active station for the last year of 
#data. Return a JSON list of temperature observations (TOBS) for the previous year.
@app.route('/api/v1.0/tobs')
def tobs():
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    year = most_recent_date[0].split('-')
    last_12months = dt.date(int(year[0]), int(year[1]), int(year[2])) - dt.timedelta(days = 365)
    
    last_year_temp = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= last_12months).all()
    temps= list(np.ravel(last_year_temp))
    
    return jsonify(temps)

#################################################
#Return a JSON list of the minimum temperature, the average temperature, and the max temperature 
#for a given start or start-end range. When given the start only, calculate TMIN, TAVG, and TMAX 
#for all dates greater than and equal to the start date. When given the start and the end date, 
#calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
@app.route('/api/v1.0/<start_date>')
def calc_temps(start_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    start = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).group_by(Measurement.date).all()
  
    calc_temp_dict = [{'Date': d, 'Min Temp': mi, 'Avg Temp': av, 'Max Temp': ma} for d, mi, av, ma in start]
    
    return jsonify(calc_temp_dict)
    
@app.route('/api/v1.0/<start_date>/<end_date>')
def calc_temps2(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    start_end = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).group_by(Measurement.date).all()

    calc_temp_dict = [{'Date': d, 'Min Temp': mi, 'Avg Temp': av, 'Max Temp': ma} for d, mi, av, ma in start_end]
    return jsonify(calc_temp_dict)

if __name__ == '__main__':
    app.run(debug=True)



