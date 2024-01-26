from models.allModels.Transactions.schema import (
    SchemaOutputTransactions,
    TypeTransactions,
    StatusTransactions,
)

from sqlalchemy import select
from sqlalchemy.orm import contains_eager
from sqlalchemy.ext.asyncio import AsyncSession
from models.allModels.Booking.bookingModel import Bookings
from typing import Any, List
from uuid import UUID
from pydantic import parse_obj_as


class QueryBookings:
    __dataQuery: Any
    query: Any

    def __init__(
        self,
        session: AsyncSession,
        statusJoinPublicTour: bool = False,
        statusJoinTourist: bool = False,
    ):

        self.session: AsyncSession = session
        self.query = select(Bookings)

        if statusJoinPublicTour:
            self.query = self.query.join(Bookings.publicRelationship).options(
                contains_eager(Bookings.publicRelationship)
            )

        if statusJoinTourist:
            self.query = self.query.join(Bookings.tourist).options(
                contains_eager(Bookings.tourist)
            )

    def getData(self):
        return self.__dataQuery

    async def getBookingByTout(self, tourId, statusBooking=None):
        self.__dataQuery = []

        query = self.query.where(Bookings.tourId == tourId)
        query = (
            query.where(Bookings.statusBooking == statusBooking)
            if statusBooking
            else query
        )

        BookingOnj = await self.session.execute(query)
        self.__dataQuery = BookingOnj.scalars().all()
