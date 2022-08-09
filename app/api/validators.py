from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
# from app.crud.donation import reservation_crud
from app.models import CharityProject, Donation, User


async def check_project_name_duplicate(
        project_name: str, session: AsyncSession
) -> None:
    project_id = await charity_project_crud.get_project_id_by_name(
        project_name, session
    )
    if project_id is not None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Проект с таким именем уже существует!',
        )


async def check_project_exists(
        project_id: int,
        session: AsyncSession,
) -> CharityProject:
    project = await charity_project_crud.get(project_id, session)
    if project is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Проект не найден',
        )
    return project
#
#
# async def check_reservation_intersections(**kwargs) -> None:
#     reservations = await reservation_crud.get_reservations_at_same_time(
#         **kwargs
#     )
#     if reservations:
#         raise HTTPException(
#             status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
#             detail=str(reservations),
#         )
#
#
# async def check_reservation_before_edit(
#         reservation_id: int,
#         session: AsyncSession,
#         user: User,
# ) -> Reservation:
#     reservation = await reservation_crud.get(reservation_id, session)
#     if not reservation:
#         raise HTTPException(
#             status_code=HTTPStatus.NOT_FOUND,
#             detail='Бронь не найдена!'
#         )
#     if reservation.user_id != user.id and not user.is_superuser:
#         raise HTTPException(
#             status_code=HTTPStatus.FORBIDDEN,
#             detail='Невозможно редактировать или удалить чужую бронь!'
#         )
#     return reservation
