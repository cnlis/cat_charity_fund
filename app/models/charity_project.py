from sqlalchemy import Column, String, Text

from app.core.db import Base
from app.models.financial_base import FinancialBase


class CharityProject(FinancialBase, Base):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
