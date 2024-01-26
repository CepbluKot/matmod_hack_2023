from models.allModels.Transactions.schema import (
    SchemaOutputTransactions,
    TypeTransactions,
    StatusTransactions,
)

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.allModels.Transactions.transactionsModel import Transactions
from typing import Any, List
from uuid import UUID
from pydantic import parse_obj_as


class QueryTransaction:
    __dataQuery: Any
    query: Any

    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session
        self.query = select(Transactions)

    def getData(self):
        return self.__dataQuery

    async def getTransactionsByPublicTourId(
        self,
        _publicTourId: UUID,
        typeT: TypeTransactions = None,
        statusT: StatusTransactions = None,
    ):
        self.__dataQuery = None
        self.query = self.query.where(Transactions.publicTourId == _publicTourId)
        self.query = (
            self.query.where(Transactions.typeTransactions == typeT)
            if typeT
            else self.query
        )
        self.query = (
            self.query.where(Transactions.statusTransactions == statusT)
            if statusT
            else self.query
        )

        TObj = await self.session.execute(self.query)
        TObj = TObj.scalars().all()
        self.__dataQuery = parse_obj_as(List[SchemaOutputTransactions], TObj)
