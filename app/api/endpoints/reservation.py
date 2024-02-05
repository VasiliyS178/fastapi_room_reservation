from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.reservation import ReservationCreate, ReservationDB
from app.core.db import get_async_session
from app.api.validators import check_meeting_room_exists, check_reservation_intersections, check_reservation_before_edit
from app.crud.reservation import reservation_crud


router = APIRouter()


@router.post(
    '/',
    response_model=ReservationDB
)
async def create_reservation(
    reservation: ReservationCreate,
    session: AsyncSession = Depends(get_async_session)
):
    await check_meeting_room_exists(reservation.meetingroom_id, session)
    await check_reservation_intersections(
        **reservation.dict(),
        session=session
    )
    return await reservation_crud.create(reservation, session)


@router.get(
    '/',
    response_model=list[ReservationDB]
)
async def get_all_reservations(
        session: AsyncSession = Depends(get_async_session)
):
    return await reservation_crud.get_multi(session)


@router.delete(
    '/{reservation_id}',
    response_model=ReservationDB
)
async def remove_reservation(
        reservation_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    reservation = await check_reservation_before_edit(
        reservation_id, session
    )
    reservation = await reservation_crud.remove(
        reservation, session
    )
    return reservation
