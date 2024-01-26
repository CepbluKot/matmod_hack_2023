from models.allModels.Users.schema import SchemaOutputUser
from pydantic import BaseModel

from typing import List


class SchemaGetUserForOneType(BaseModel):
    __root__: List[SchemaOutputUser]

    class Config:
        validation = False
