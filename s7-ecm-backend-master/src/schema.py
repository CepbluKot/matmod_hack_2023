# Contains pydantic schemas

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from typing import List


class AircraftFilter(BaseModel):
    aircraft_grp: str
    aircraft_type: str
    aircraft_family: str
    ac_manufacturer: str


class EngineFilter(BaseModel):
    engine_type: str
    engine_family: str
    manufacturer: str


class FilterBody(BaseModel):
    aircraft: AircraftFilter | None = None
    engine: EngineFilter | None = None
    flight_phase: str
    datetime_start: datetime
    datetime_end: datetime


class MLInputX(BaseModel):
    engine_id: Optional[str] = None
    aircraft_id: Optional[str] = None
    flight_datetime: Optional[str] = None
    flight_phase: Optional[str] = None
    engine_position: Optional[float] = None
    n1_modifier: Optional[float] = None
    number_blades: Optional[float] = None
    engine_family: Optional[str] = None
    engine_type: Optional[str] = None
    manufacturer: Optional[str] = None
    ZHPTAC: Optional[float] = None
    ZLPTAC: Optional[float] = None
    ZPCN12: Optional[float] = None
    ZPCN25: Optional[float] = None
    ZPHSF: Optional[float] = None
    ZPHSR: Optional[float] = None
    ZPN12R: Optional[float] = None
    ZPOIL: Optional[float] = None
    ZPS3: Optional[float] = None
    ZT1AB: Optional[float] = None
    ZT3: Optional[float] = None
    ZT49: Optional[float] = None
    ZTAMB: Optional[float] = None
    ZTLA: Optional[float] = None
    ZTNAC: Optional[float] = None
    ZTOIL: Optional[float] = None
    ZVB1F: Optional[float] = None
    ZVB1R: Optional[float] = None
    ZVB2F: Optional[float] = None
    ZVB2R: Optional[float] = None
    ZVSV: Optional[float] = None
    ZWF36: Optional[float] = None
    IHPSOV: Optional[float] = None
    aircraft_family: Optional[str] = None
    aircraft_type: Optional[str] = None
    aircraft_grp: Optional[str] = None
    ac_manufacturer: Optional[str] = None
    AGW: Optional[float] = None
    CAS: Optional[float] = None
    IAI: Optional[float] = None
    IVS12: Optional[float] = None
    SAT: Optional[float] = None
    ZALT: Optional[float] = None
    ZT1A: Optional[float] = None
    ZVIAS: Optional[float] = None
    ZWBP1: Optional[float] = None
    ZWBP1_8E: Optional[float] = None
    ZWBP2: Optional[float] = None
    ZWBP2_8E: Optional[float] = None
    ZXM: Optional[float] = None
    IBE: Optional[float] = None
    IBP: Optional[float] = None
    IAIE: Optional[float] = None
    DEGT: Optional[float] = None
    DELFN: Optional[float] = None
    DELN1: Optional[float] = None
    DELVSV: Optional[float] = None
    DPOIL: Optional[float] = None
    EGTC: Optional[float] = None
    EGTHDM: Optional[float] = None
    EGTHDM_D: Optional[float] = None
    GEGTMC: Optional[float] = None
    GN2MC: Optional[float] = None
    GPCN25: Optional[float] = None
    GWFM: Optional[float] = None
    PCN12: Optional[float] = None
    PCN12I: Optional[float] = None
    PCN1AR: Optional[float] = None
    PCN1BR: Optional[float] = None
    PCN1K: Optional[float] = None
    PCN2C: Optional[float] = None
    SLOATL: Optional[float] = None
    SLOATL_D: Optional[float] = None
    VSVNOM: Optional[float] = None
    WBE: Optional[float] = None
    WBI: Optional[float] = None
    WFMP: Optional[float] = None
    ZPCN25_D: Optional[float] = None
    ZT49_D: Optional[float] = None
    ZTLA_D: Optional[float] = None
    ZTNAC_D: Optional[float] = None
    ZWF36_D: Optional[float] = None
    id: Optional[int] = None

    class Config:
        use_enum_values = True
        allow_population_by_field_name = True
        orm_mode = True

class MLOutputY(BaseModel):
    BRAT: Optional[float] = None
    DEGT: Optional[float] = None
    DELFN: Optional[float] = None
    DELN1: Optional[float] = None
    DELVSV: Optional[float] = None
    DPOIL: Optional[float] = None
    EGTC: Optional[float] = None
    EGTHDM: Optional[float] = None
    EGTHDM_D: Optional[float] = None
    GEGTMC: Optional[float] = None
    GN2MC: Optional[float] = None
    GPCN25: Optional[float] = None
    GWFM: Optional[float] = None
    PCN12: Optional[float] = None
    PCN12I: Optional[float] = None
    PCN1AR: Optional[float] = None
    PCN1BR: Optional[float] = None
    PCN1K: Optional[float] = None
    PCN2C: Optional[float] = None
    SLOATL: Optional[float] = None
    SLOATL_D: Optional[float] = None

    WBE: Optional[float] = None
    WBI: Optional[float] = None
    WFMP: Optional[float] = None
    ZPCN25_D: Optional[float] = None
    ZT49_D: Optional[float] = None
    ZTLA_D: Optional[float] = None
    ZTNAC_D: Optional[float] = None
    ZWF36_D: Optional[float] = None

    class Config:
        use_enum_values = True
        allow_population_by_field_name = True
        orm_mode = True
