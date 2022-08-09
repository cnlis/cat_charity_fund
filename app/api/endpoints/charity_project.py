from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (check_project_exists,
                                check_project_name_duplicate)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.charity_project import charity_project_crud
# from app.crud.donation import reservation_crud
from app.schemas.charity_project import (CharityProjectCreate, CharityProjectDB,
                                         CharityProjectUpdate)
from app.schemas.donation import DonationDB

router = APIRouter()


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def create_new_project(
        project: CharityProjectCreate,
        session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров."""
    await check_project_name_duplicate(project.name, session)
    project = await charity_project_crud.create(project, session)
    return project


@router.get(
    '/',
    response_model=list[CharityProjectDB],
    response_model_exclude_none=True,
)
async def get_all_projects(
        session: AsyncSession = Depends(get_async_session),
):
    all_rooms = await charity_project_crud.get_multi(session)
    return all_rooms


@router.patch(
    '/{project_id}',
    response_model=CharityProjectDB,
    # response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def partially_update_project(
        project_id: int,
        obj_in: CharityProjectUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров."""
    project = await check_project_exists(project_id, session)
    if obj_in.name is not None:
        await check_project_name_duplicate(obj_in.name, session)
    project = await charity_project_crud.update(
        project, obj_in, session
    )
    return project


@router.delete(
    '/{project_id}',
    response_model=CharityProjectDB,
    # response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def remove_project(
        project_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров."""
    meeting_room = await check_project_exists(project_id, session)
    meeting_room = await charity_project_crud.remove(meeting_room, session)
    return meeting_room
#
#
# @router.get(
#     '/{meeting_room_id}/reservations',
#     response_model=list[ReservationDB],
#     response_model_exclude={'user_id'},
# )
# async def get_reservations_for_room(
#         meeting_room_id: int,
#         session: AsyncSession = Depends(get_async_session),
# ):
#     await check_meeting_room_exists(meeting_room_id, session)
#     reservations = await reservation_crud.get_future_reservations_for_room(
#         meeting_room_id, session
#     )
#     return reservations
