from datetime import datetime
from sqlalchemy import Datetime, Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    created_at = Column(Datetime, default=datetime.now(), nullable=False)
