from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

# from app.api.validators import (check_meeting_room_exists,
#                                 check_reservation_before_edit,
#                                 check_reservation_intersections)
from app.core.db import get_async_session
from app.core.user import current_user, current_superuser
from app.crud.donation import donation_crud
from app.models import User
from app.schemas.donation import (DonationCreate, DonationDB,
                                  DonationSuperuserDB)

router = APIRouter()


@router.post(
    '/',
    response_model=DonationDB,
    response_model_exclude_none=True,
)
async def create_donation(
        donation: DonationCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    # await check_meeting_room_exists(
    #     reservation.meetingroom_id, session
    # )
    # await check_reservation_intersections(
    #     **reservation.dict(), session=session
    # )
    new_donation = await donation_crud.create(donation, session, user)
    return new_donation


@router.get(
    '/',
    response_model=list[DonationSuperuserDB],
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def get_all_donations(
        session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров."""
    all_donations = await donation_crud.get_multi(session)
    return all_donations


@router.get(
    '/my',
    response_model=list[DonationDB],
    response_model_exclude={'user_id'},
    response_model_exclude_none=True,
)
async def get_my_donations(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    """Получает список всех пожертвований для текущего пользователя."""
    donations = await donation_crud.get_by_user(user.id, session)
    return donations
