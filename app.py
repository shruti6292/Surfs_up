#import pandas dependancies
import datetime as dt
import numpy as np
import pandas as pd

#import SQLAlchemy dependancies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#import FLASK dependencies 
from flask import Flask, jsonify

#set up database
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

#set up Flask
app = Flask(__name__)

#Notice the __name__ variable in this code. This is a special type of variable in Python. Its value depends on where and how the code is run. For example, if we wanted to import our app.py file into another Python file named example.py, the variable __name__ would be set to example. 
# Here's an example of what that might look like:
# import app
# print("example __name__ = %s", __name__)
# if __name__ == "__main__":
#     print("example is being run directly.")
# else:
#     print("example is being imported")

#Create the Welcome Route
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!<br><br>
    Available Routes:<br>
    /api/v1.0/precipitation<br>
    /api/v1.0/stations<br>
    /api/v1.0/tobs<br>
    /api/v1.0/temp/start/end<br>
    ''')

#Precipitation Route
@app.route("/api/v1.0/precipitation")
# def precipitation():
#     return

#calculates the date one year ago from the most recent date in the database.
# def precipitation():
#    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#    return

#to get the date and precipitation for the previous year
# def precipitation():
#    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#    precipitation = session.query(Measurement.date, Measurement.prcp).\
#       filter(Measurement.date >= prev_year).all()
#    return
#create a dictionary with the date as the key and the precipitation as the value
# "jsonify" our dictionary.
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

#Stations Route
@app.route("/api/v1.0/stations")
#a new function called stations()
# def stations():
#     return
#to create a query that will allow us to get all of the stations in our database
# def stations():
#     results = session.query(Station.station).all()
#     return
#unravel the results, convert it into list,jasonify the list
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

#Monthly Temperature Route
@app.route("/api/v1.0/tobs")
#create a function called temp_monthly()
# def temp_monthly():
#     return
#calculate the date one year ago from the last date in the database.
# def temp_monthly():
#     prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#     return
#query the primary station for all the temperature observations from the previous year
# def temp_monthly():
#     prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#     results = session.query(Measurement.tobs).\
#         filter(Measurement.station == 'USC00519281').\
#         filter(Measurement.date >= prev_year).all()
#     return
#unravel the results, convert it into list,jasonify the list
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

#Statistics Route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
# def stats():
#      return
# def stats(start=None, end=None):
#      return
# def stats(start=None, end=None):
#     sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
# def stats(start=None, end=None):
#     sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

#     if not end:
#         results = session.query(*sel).\
#             filter(Measurement.date >= start).all()
#         temps = list(np.ravel(results))
#         return jsonify(temps=temps)
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

if __name__ == "__main__":
    app.run()