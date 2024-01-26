import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


# DB Connection, endpoints
import datetime
import json
from ml_requests import *
import asyncio
import dateutil.parser
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import FastAPI, UploadFile, BackgroundTasks, File, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine, MetaData, func, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from sqlalchemy.orm import Session
import csv
import codecs
from typing import Dict, List
from schema import MLOutputY
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from models import FlightPhase

from enum import Enum

from utils import columns_to_dict, groupData

from models import *

from schema import *




# Database connection
DATABASE_URL = 'postgresql://postgres:kirill@localhost/s7-ecm-engines'
metadata = MetaData()

engine = create_engine(DATABASE_URL, connect_args={}, pool_pre_ping=True)  # pool_pre_ping needed for db tests

app = FastAPI()

# CORS
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def connect_db():
    session = Session(bind=engine)
    return session


# Endpoints for .scv tables upload
@app.post("/api/frontend/upload_x")
def upload_x(background_tasks: BackgroundTasks, file: UploadFile = File(...), db: Session = Depends(connect_db)):
    all_data = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))  # JSON object csv_reader
    background_tasks.add_task(file.file.close)

    parsed = []
    for row in list(all_data):
        for col in row:
            conv = lambda i: i or None
            row[col] = conv(row[col])

        row['flight_datetime'] = dateutil.parser.parse(row['flight_datetime']).replace(second=0, microsecond=0)

        parsed.append(X(row))
        db.add(X(row))
        db.commit()
    return "ok"


@app.post("/api/frontend/upload_y")
def upload_y(background_tasks: BackgroundTasks, file: UploadFile = File(...), db: Session = Depends(connect_db)):
    all_data = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))  # JSON object csv_reader
    background_tasks.add_task(file.file.close)

    parsed = []
    for row in list(all_data):
        for col in row:
            conv = lambda i: i or None
            row[col] = conv(row[col])

        row['flight_datetime'] = dateutil.parser.parse(row['flight_datetime']).replace(second=0, microsecond=0)

        parsed.append(Y(row))
        db.add(Y(row))
        db.commit()
    return "ok"


# Endpoints to get frontend data ranges
@app.get("/api/frontend/filters_data")
def getAirAircraftGroups(db: Session = Depends(connect_db)):
    aircraft_filters_data = []
    engine_filters_data = []

    for aircraft in db.query(X).distinct(X.aircraft_grp):

        engines = []
        for engine in db.query(X).filter(X.aircraft_grp == aircraft.aircraft_grp).distinct(X.engine_type):
            engines.append({
                "engine_type": engine.engine_type,
                "engine_family": engine.engine_family,
                "manufacturer": engine.manufacturer
            })

        aircraft_filters_data.append({
            "aircraft_grp": aircraft.aircraft_grp,
            "aircraft_type": aircraft.aircraft_type,
            "aircraft_family": aircraft.aircraft_family,
            "ac_manufacturer": aircraft.ac_manufacturer,
            "engines": engines
        })

    for engine in db.query(X).distinct(X.engine_type):

        aircrafts = []
        for aircraft in db.query(X).filter(X.engine_type == engine.engine_type).distinct(X.aircraft_grp):
            aircrafts.append({
                "aircraft_grp": aircraft.aircraft_grp,
                "aircraft_family": aircraft.aircraft_family,
                "ac_manufacturer": aircraft.ac_manufacturer,
                "aircraft_type": aircraft.aircraft_type
            })

        engine_filters_data.append({
            "engine_type": engine.engine_type,
            "engine_family": engine.engine_family,
            "manufacturer": engine.manufacturer,  # Engine manufacturer
            "aircrafts": aircrafts
        })
    datetime_min = db.query(func.min(X.flight_datetime)).first()[0]
    datetime_max = db.query(func.max(X.flight_datetime)).first()[0]

    return {
        "aircraft": aircraft_filters_data,
        "engine": engine_filters_data,
        "time_range": {
            "min": datetime_min,
            "max": datetime_max
        }
    }


@app.get("/api/frontend/datetime_range")  # for delete
def getTimeRange(db: Session = Depends(connect_db)):
    datetime_min = db.query(func.min(X.flight_datetime)).first()[0]
    datetime_max = db.query(func.max(X.flight_datetime)).first()[0]

    return {
        "min": datetime_min,
        "max": datetime_max
    }


# Endpoints for filtration
@app.post("/api/frontend/filter")
def filterByParams(filterBody: FilterBody, db: Session = Depends(connect_db)):
    if filterBody.aircraft is None:
        data_x_unsorted = db.query(X).filter(
            X.engine_type == filterBody.engine.engine_type,
            X.engine_family == filterBody.engine.engine_family,
            X.manufacturer == filterBody.engine.manufacturer,
            X.flight_phase == filterBody.flight_phase,
            X.flight_datetime >= filterBody.datetime_start,
            X.flight_datetime <= filterBody.datetime_end
        ).all()
    elif filterBody.engine is None:
        data_x_unsorted = db.query(X).filter(
            X.aircraft_grp == filterBody.aircraft.aircraft_grp,
            X.aircraft_type == filterBody.aircraft.aircraft_type,
            X.aircraft_family == filterBody.aircraft.aircraft_family,
            X.ac_manufacturer == filterBody.aircraft.ac_manufacturer,
            X.flight_phase == filterBody.flight_phase,
            X.flight_datetime >= filterBody.datetime_start,
            X.flight_datetime <= filterBody.datetime_end
        ).all()
    else:
        data_x_unsorted = db.query(X).filter(
            X.aircraft_grp == filterBody.aircraft.aircraft_grp,
            X.aircraft_type == filterBody.aircraft.aircraft_type,
            X.aircraft_family == filterBody.aircraft.aircraft_family,
            X.ac_manufacturer == filterBody.aircraft.ac_manufacturer,
            X.engine_type == filterBody.engine.engine_type,
            X.engine_family == filterBody.engine.engine_family,
            X.manufacturer == filterBody.engine.manufacturer,
            X.flight_phase == filterBody.flight_phase,
            X.flight_datetime >= filterBody.datetime_start,
            X.flight_datetime <= filterBody.datetime_end
        ).all()




    grouped_data_x = groupData(data_x_unsorted)

    grouped_data_y = grouped_data_x

    for aircraft_id in grouped_data_y:
        for engine_id in grouped_data_y[aircraft_id]:
            for row in grouped_data_y[aircraft_id][engine_id]:
                row_index = grouped_data_y[aircraft_id][engine_id].index(row)

                grouped_data_y[aircraft_id][engine_id][row_index] = db.query(Y).filter(
                    Y.engine_id == row['engine_id'],
                    Y.flight_datetime == row['flight_datetime'],
                    Y.flight_phase == row['flight_phase']
                ).first()

    resp = sendFilteredDataX(data_x_unsorted)  # send JSON with selected rows from X to ML service

    # add wait func performance
    graph_data = []

    data: Dict[str, Dict[str, List[MLOutputY]]] = resp.text

    parsed = {}
    data = json.loads(data)


    for ac_id in grouped_data_x:
        for eng_id in grouped_data_x[ac_id]:

            x_arr = grouped_data_x[ac_id][eng_id]
            y_arr = grouped_data_y[ac_id][eng_id]

            if not ac_id in parsed:
                parsed[ac_id] = {}

            if not eng_id in parsed[ac_id]:
                parsed[ac_id][eng_id] = {}

            parsed[ac_id][eng_id]["predicted"] = []
            parsed[ac_id][eng_id]["real"] = []

            for x_data in x_arr:

                x_data_parsed = columns_to_dict(x_data)

                x_data_parsed['flight_datetime'] = str(x_data_parsed['flight_datetime'])
                x_data_parsed['flight_phase'] = str(x_data_parsed['flight_phase'])

                parsed[ac_id][eng_id]["real"].append(x_data_parsed)

            for y_data in y_arr:

                y_data_parsed = columns_to_dict(y_data)
                y_data_parsed['flight_datetime'] = str(y_data_parsed['flight_datetime'])
                y_data_parsed['flight_phase'] = str(y_data_parsed['flight_phase'])

                parsed[ac_id][eng_id]["predicted"].append(y_data_parsed)

    # parsed = json.dumps(parsed)

    print('parsed', parsed)

    return parsed



#  ---         ---

# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
