# Models for database tables
import enum

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()  # we will inherit from this class to create the ORM models


class FlightPhase(enum.Enum):
    TAKEOFF = 'TAKEOFF'
    CRUISE = 'CRUISE'


class X(Base):
    __tablename__ = "X"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    engine_id = Column(String, nullable=False, index=True)
    aircraft_id = Column(String, nullable=False, index=True)
    flight_datetime = Column(DateTime, nullable=False, index=True)  # уточнить про тип данных --Save as DateTime and
    # import from csv for postgres---
    flight_phase = Column(Enum(FlightPhase), nullable=False, index=True)  # Changed to Enum type
    engine_position = Column(Integer, nullable=False)
    n1_modifier = Column(Integer, nullable=False)
    number_blades = Column(Integer, nullable=False)
    engine_family = Column(String, nullable=False, index=True)
    engine_type = Column(String, nullable=False, index=True)
    manufacturer = Column(String, nullable=False, index=True)
    ZHPTAC = Column(Float)
    ZLPTAC = Column(Float)
    ZPCN12 = Column(Float)
    ZPCN25 = Column(Float)
    ZPHSF = Column(Float)
    ZPHSR = Column(Float)
    ZPN12R = Column(Float)
    ZPOIL = Column(Float)
    ZPS3 = Column(Float)
    ZT1AB = Column(Float)
    ZT3 = Column(Float)
    ZT49 = Column(Float)
    ZTAMB = Column(Float)
    ZTLA = Column(Float)
    ZTNAC = Column(Float)
    ZTOIL = Column(Float)
    ZVB1F = Column(Float)
    ZVB1R = Column(Float)
    ZVB2F = Column(Float)
    ZVB2R = Column(Float)
    ZVSV = Column(Float)
    ZWF36 = Column(Float)
    IHPSOV = Column(Integer)
    aircraft_family = Column(String)
    aircraft_type = Column(String)
    aircraft_grp = Column(String)
    ac_manufacturer = Column(String)
    AGW = Column(Float)
    CAS = Column(Float)
    IAI = Column(Integer)
    IVS12 = Column(Integer)
    SAT = Column(Float)
    ZALT = Column(Float)
    ZT1A = Column(Float)
    ZVIAS = Column(Float)
    ZWBP1 = Column(Float)
    ZWBP1_8E = Column(Float)
    ZWBP2 = Column(Float)
    ZWBP2_8E = Column(Float)
    ZXM = Column(Float)
    IBE = Column(Integer)
    IBP = Column(Integer)
    IAIE = Column(Integer)

    def __init__(self, dataObj: dict):
        self.__dict__.update(dataObj)


class Y(Base):
    __tablename__ = "Y"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    flight_datetime = Column(DateTime, nullable=False, index=True)  # уточнить про тип данных --Save as DateTime
    flight_phase = Column(Enum(FlightPhase), nullable=False, index=True)
    engine_id = Column(String, nullable=False, index=True)
    BRAT = Column(Float)
    DEGT = Column(Float)
    DELFN = Column(Float)
    DELN1 = Column(Float)
    DELVSV = Column(Float)
    DPOIL = Column(Float)
    EGTC = Column(Float)
    EGTHDM = Column(Float)
    EGTHDM_D = Column(Float)
    GEGTMC = Column(Float)
    GN2MC = Column(Float)
    GPCN25 = Column(Float)
    GWFM = Column(Float)
    PCN12 = Column(Float)
    PCN12I = Column(Float)
    PCN1AR = Column(Float)
    PCN1BR = Column(Float)
    PCN1K = Column(Float)
    PCN2C = Column(Float)
    SLOATL = Column(Float)
    SLOATL_D = Column(Float)
    VSVNOM = Column(Float)
    WBE = Column(Float)
    WBI = Column(Float)
    WFMP = Column(Float)
    ZPCN25_D = Column(Float)
    ZT49_D = Column(Float)
    ZTLA_D = Column(Float)
    ZTNAC_D = Column(Float)
    ZWF36_D = Column(Float)

    def __init__(self, dataObj: dict):
        self.__dict__.update(dataObj)
