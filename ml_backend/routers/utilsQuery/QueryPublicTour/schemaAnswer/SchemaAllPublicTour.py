from pydantic import BaseModel
from typing import List

from models.allModels.PublicTour.schema import SchemaOutPublicTours


class SchemaAllPublicTour(BaseModel):
    __root__: List[SchemaOutPublicTours]
