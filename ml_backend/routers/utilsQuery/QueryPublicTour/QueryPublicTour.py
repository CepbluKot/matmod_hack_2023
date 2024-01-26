from models.allModels.PublicTour.publicToursModel import PublicTours
from .schemaAnswer.SchemaAllPublicTour import SchemaAllPublicTour

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from typing import Any, List
from datetime import datetime, timezone
from uuid import UUID


class QueryPublicTour:
    __dataQuery: Any
    query: Any

    def __init__(self, session: AsyncSession, userId=None, deleteStatus=False):
        self.session: AsyncSession = session
        self.userId: userId

        if userId:
            self.query = select(PublicTours).where(PublicTours.creatorId == userId)
        else:
            self.query = select(PublicTours)
        self.query = (
            self.query.where(PublicTours.deleteStatus != True)
            if not deleteStatus
            else self.query
        )

    def getData(self):
        return self.__dataQuery

    async def getTourInOperator(self, listPublicTourId):
        self.__dataQuery = None

        toursObj = await self.session.execute(
            self.query.where(PublicTours.id.in_(listPublicTourId))
        )
        toursObj = toursObj.scalars().all()
        self.__dataQuery = SchemaAllPublicTour.parse_obj(toursObj)

    async def getByTourIdFilterDate(self, tourId: UUID, dateStartLe: datetime = None):
        self.__dataQuery = None

        self.query = self.query.where(PublicTours.tourId == tourId)
        self.query = (
            self.query.where(PublicTours.dtStart >= dateStartLe)
            if dateStartLe
            else self.query
        )

        toursObj = await self.session.execute(self.query)
        self.__dataQuery = toursObj.scalars().all()
