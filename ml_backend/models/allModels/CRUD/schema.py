from pydantic import BaseModel, Field
from typing import Optional, Dict


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


class MLOutputYFull(MLOutputY):    
    engine_id: Optional[str] = None
    id: Optional[int] = None
    flight_datetime: Optional[str] = None
    flight_phase: Optional[str] = None
        
    class Config:
        use_enum_values = True
        allow_population_by_field_name = True
        orm_mode = True



class MLInputX(BaseModel): 
    engine_id: Optional[str] = Field(..., nullable=True)
    aircraft_id: Optional[str] = Field(..., nullable=True)
    flight_datetime: Optional[str] = Field(..., nullable=True)
    flight_phase: Optional[str] = Field(..., nullable=True)
    engine_position: Optional[float] = Field(..., nullable=True)
    n1_modifier: Optional[float] = Field(..., nullable=True)
    number_blades: Optional[float] = Field(..., nullable=True)
    engine_family: Optional[str] = Field(..., nullable=True)
    engine_type: Optional[str] = Field(..., nullable=True)
    manufacturer: Optional[str] = Field(..., nullable=True)
    ZHPTAC: Optional[float] = Field(..., nullable=True)
    ZLPTAC: Optional[float] = Field(..., nullable=True)
    ZPCN12: Optional[float] = Field(..., nullable=True)
    ZPCN25: Optional[float] = Field(..., nullable=True)
    ZPHSF: Optional[float] = Field(..., nullable=True)
    ZPHSR: Optional[float] = Field(..., nullable=True)
    ZPN12R: Optional[float] = Field(..., nullable=True)
    ZPOIL: Optional[float] = Field(..., nullable=True)
    ZPS3: Optional[float] = Field(..., nullable=True)
    ZT1AB: Optional[float] = Field(..., nullable=True)
    ZT3: Optional[float] = Field(..., nullable=True)
    ZT49: Optional[float] = Field(..., nullable=True)
    ZTAMB: Optional[float] = Field(..., nullable=True)
    ZTLA: Optional[float] = Field(..., nullable=True)
    ZTNAC: Optional[float] = Field(..., nullable=True)
    ZTOIL: Optional[float] = Field(..., nullable=True)
    ZVB1F: Optional[float] = Field(..., nullable=True)
    ZVB1R: Optional[float] = Field(..., nullable=True)
    ZVB2F: Optional[float] = Field(..., nullable=True)
    ZVB2R: Optional[float] = Field(..., nullable=True)
    ZVSV: Optional[float] = Field(..., nullable=True)
    ZWF36: Optional[float] = Field(..., nullable=True)
    IHPSOV: Optional[float] = Field(..., nullable=True)
    aircraft_family: Optional[str] = Field(..., nullable=True)
    aircraft_type: Optional[str] = Field(..., nullable=True)
    aircraft_grp: Optional[str] = Field(..., nullable=True)
    ac_manufacturer: Optional[str] = Field(..., nullable=True)
    AGW: Optional[float] = Field(..., nullable=True)
    CAS: Optional[float] = Field(..., nullable=True)
    IAI: Optional[float] = Field(..., nullable=True)
    IVS12: Optional[float] = Field(..., nullable=True)
    SAT: Optional[float] = Field(..., nullable=True)
    ZALT: Optional[float] = Field(..., nullable=True)
    ZT1A: Optional[float] = Field(..., nullable=True)
    ZVIAS: Optional[float] = Field(..., nullable=True)
    ZWBP1: Optional[float] = Field(..., nullable=True)
    ZWBP1_8E: Optional[float] = Field(..., nullable=True)
    ZWBP2: Optional[float] = Field(..., nullable=True)
    ZWBP2_8E: Optional[float] = Field(..., nullable=True)
    ZXM: Optional[float] = Field(..., nullable=True)
    IBE: Optional[float] = Field(..., nullable=True)
    IBP: Optional[float] = Field(..., nullable=True)
    IAIE: Optional[float] = Field(..., nullable=True)
    id: Optional[int] = Field(..., nullable=True)

    class Config:
        use_enum_values = True
        allow_population_by_field_name = True
        orm_mode = True


class MLInputXFiltered(BaseModel): # to-do - fix
    n1_modifier: Optional[float] = None
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


    class Config:
        use_enum_values = True
        allow_population_by_field_name = True
        orm_mode = True
