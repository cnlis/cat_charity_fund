from datetime import datetime
from typing import Optional

from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.donation import Donation


class CRUDDonation(CRUDBase):

    # async def get_reservations_at_same_time(
    #         self,
    #         *,
    #         from_reserve: datetime,
    #         to_reserve: datetime,
    #         meetingroom_id: int,
    #         reservation_id: Optional[int] = None,
    #         session: AsyncSession,
    # ) -> list[Reservation]:
    #     select_statement = select(Reservation).where(
    #         Reservation.meetingroom_id == meetingroom_id,
    #         and_(
    #             from_reserve <= Reservation.to_reserve,
    #             to_reserve >= Reservation.from_reserve
    #         )
    #     )
    #     if reservation_id is not None:
    #         select_statement = select_statement.where(
    #             Reservation.id != reservation_id
    #         )
    #     reservations = await session.execute(select_statement)
    #     return reservations.scalars().all()
    #
    # async def get_future_reservations_for_room(
    #         self,
    #         room_id: int,
    #         session: AsyncSession
    # ) -> list[Reservation]:
    #     select_statement = select(Reservation).where(
    #         Reservation.meetingroom_id == room_id,
    #         Reservation.to_reserve > datetime.now()
    #     )
    #     reservations = await session.execute(select_statement)
    #     return reservations.scalars().all()
    #
    async def get_by_user(
            self,
            user_id: int,
            session: AsyncSession
    ) -> list[Donation]:
        select_statement = select(Donation).where(
            Donation.user_id == user_id
        )
        reservations = await session.execute(select_statement)
        return reservations.scalars().all()


donation_crud = CRUDDonation(Donation)
