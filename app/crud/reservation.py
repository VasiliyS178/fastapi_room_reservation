from typing import Optional
from datetime import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import and_
from app.crud.base import CRUDBase
from app.models.reservation import Reservation


class CRUDReservation(CRUDBase):

    async def get_reservations_at_the_same_time(
        self,
        from_reserve: datetime,
        to_reserve: datetime,
        meetingroom_id: int,
        session: AsyncSession
    ) -> Optional[list[Reservation]]:
        reservations = await session.execute(
            select(Reservation).where(
                Reservation.meetingroom_id == meetingroom_id,
                and_(
                    from_reserve <= Reservation.to_reserve,
                    to_reserve >= Reservation.from_reserve
                )
            )
        )
        return reservations.scalars().all()


reservation_crud = CRUDReservation(Reservation)
