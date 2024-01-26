from models.allModels.Users.userModel import Users
from models.allModels.Users.schema import SchemaOutputUser

from sqlalchemy import select
from pydantic import parse_obj_as
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, List
from .schemaAnswer.SchemaGetUserForOneType import SchemaGetUserForOneType


class QueryUsers:
    __dataQuery: Any

    def __init__(self, session: AsyncSession, userId=None):
        self.session: AsyncSession = session
        self.userId: userId

    def getData(self):
        return self.__dataQuery

    async def getUserForOneType(self, typeUser, typeObj=None):
        self.__dataQuery = None

        allUsers = await self.session.execute(
            select(Users).where(
                Users.typeUser == typeUser, Users.statusVerfyCode == True
            )
        )
        allUsers: Users = allUsers.scalars().all()
        self.__dataQuery: SchemaGetUserForOneType = (
            SchemaGetUserForOneType.parse_obj(allUsers)
            if typeObj is None
            else parse_obj_as(List[typeObj], allUsers)
        )
