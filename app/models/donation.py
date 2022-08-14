from sqlalchemy import Column, ForeignKey, Integer, Text

from app.core.db import Base
from app.models.financial_base import FinancialBase


class Donation(FinancialBase, Base):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)
