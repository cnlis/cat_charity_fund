from datetime import datetime

from sqlalchemy import not_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CharityProject, Donation


async def invest(source, session: AsyncSession):
    dest_model = CharityProject if isinstance(source, Donation) else Donation

    partly_invested = await session.execute(
        select(dest_model).where(
            not_(dest_model.fully_invested)
        ).order_by(dest_model.create_date)
    )
    partly_invested = partly_invested.scalars().all()

    for item in partly_invested:
        item_remainder = item.full_amount - item.invested_amount
        source_remainder = source.full_amount - source.invested_amount
        if not source_remainder:
            break

        if item_remainder <= source_remainder:
            source.invested_amount += item_remainder
            item.invested_amount = item.full_amount
            item.fully_invested = True
            item.close_date = datetime.now()
        else:
            item.invested_amount += source_remainder
            source.invested_amount = source.full_amount
        session.add(item)

    if source.invested_amount == source.full_amount:
        source.fully_invested = True
        source.close_date = datetime.now()

    session.add(source)
    await session.commit()
    await session.refresh(source)
    return source
