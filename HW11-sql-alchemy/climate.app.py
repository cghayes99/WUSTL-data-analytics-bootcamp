#!/opt/anaconda3/bin/python

'''
###################################################################################
# @script   Surfs Up! - Climate  climate.app.py                                   #
# @version  1.0.0                                                                 #
#---------------------------------------------------------------------------------#
# FLASK API for Surfs Up!- Analysis                                               #
#                                                                                 #
# Modification History                                                            #
#                                                                                 #
# Date        Name             Description                                        #
# ----------  -----------      ----------------------------------                 #
# 2018/08/30  (chris)          Original script                                    #
#                                                                                 #
###################################################################################
'''

## Imports
import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

## SQL init
engine = create_engine('sqlite:///Resources/hawaii.sqlite')
Base = automap_base()
Base.prepare(engine, reflect=True)

Station = Base.classes.station
Measurement = Base.classes.measurement
session = Session(engine)

## FLASH init
app = Flask(__name__)

## Constants
end_date   = '2017-08-23'
start_date = '2016-08-23'

## Functions

'''
    /api/v1.0/precipitation
     
'''
@app.route("/api/v1.0/precipitation")
def precipitation():
    sql_results = session.query(Measurement.date, Measurement.prcp) \
                         .filter(Measurement.date >= start_date) \
                         .filter(Measurement.date <= end_date) \
                         .filter(Measurement.prcp != None) \
                         .order_by(Measurement.date.asc()).statement
    
    dfs = pd.read_sql_query(sql_results, session.bind)
    df = pd.DataFrame(dfs.groupby(['date']).sum())
    
    df_keys = df.index.values.tolist()
    df_values = df['prcp'].tolist()
    
    df_dict = dict(zip(df_keys, df_values))
    return jsonify(df_dict)

'''
    /api/v1.0/stations
     
'''
@app.route("/api/v1.0/stations")
def stations():
    sql_results = session.query(Station.station, Station.name, Station.latitude, Station.longitude) \
                         .order_by(Station.station.asc()) \
                         .statement
    
    df = pd.read_sql_query(sql_results, session.bind)
    df_list = df.values.tolist()    
    return jsonify(df_list)
    
'''
    /api/v1.0/tobs
     
'''
@app.route("/api/v1.0/tobs")
def tobs():
    sql_results = session.query(Measurement.date, Measurement.station, Station.name, Measurement.tobs) \
                         .filter(Measurement.station == Station.station) \
                         .filter(Measurement.date >= start_date) \
                         .filter(Measurement.date <= end_date) \
                         .statement    
    
    df = pd.read_sql_query(sql_results, session.bind)
    df_list = df.values.tolist()    
    return jsonify(df_list)
    
'''
    /api/v1.0/<start>
    /api/v1.0/<start>/<end>
     
'''
@app.route("/api/v1.0/<start>")
def range_start(start):
    sql_results = session.query(func.avg(Measurement.tobs), \
                                func.max(Measurement.tobs), \
                                func.min(Measurement.tobs)) \
                         .filter(Measurement.date >= start) \
                         .statement
    
    df = pd.read_sql_query(sql_results, session.bind)
    
    tavg = int(df['avg_1'])
    tmax = int(df['max_1'])
    tmin = int(df['min_1'])
    
    dict = {'average temperature':tavg, 'minimum temperature':tmin, 'max temperature':tmax}    
    return jsonify(dict)

@app.route("/api/v1.0/<start>/<end>")
def range_start_end(start, end):
    sql_results = session.query(func.avg(Measurement.tobs), \
                                func.max(Measurement.tobs), \
                                func.min(Measurement.tobs)) \
                         .filter(Measurement.date >= start) \
                         .filter(Measurement.date <= end) \                         
                         .statement
    
    df = pd.read_sql_query(sql_results, session.bind)
    
    tavg = int(df['avg_1'])
    tmax = int(df['max_1'])
    tmin = int(df['min_1'])
    
    dict = {'average temperature':tavg, 'minimum temperature':tmin, 'max temperature':tmax}    
    return jsonify(dict)

'''
    /
     
'''
@app.route("/")
def root_path():
    intro = (
             '<h4>Surfs Up! - Climate</h4'
             '<p>Avalable Routes:</p>'
             '<code>/api/v1.0/precipitation</code> -- precipitation from the previous year</br>'
             '<code>/api/v1.0/stations</code> -- listing of stations</br>'
             '<code>/api/v1.0/tobs</code> -- temperature observations from the previous year</br>'
             '<code>/api/v1.0/<start date></code></br>'
             '<code>/api/v1.0/<start date/<end date></code> -- average, minimum and max temperature for a given date range</br>')
    return (intro)

## Main functionality
if __name__ == '__main__':
    app.run(debug=True)


