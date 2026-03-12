from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, String, text
from sqlalchemy.orm import mapped_column
from app.db.base import Base


class User(Base):

    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True, index=True)
    username = mapped_column(String(50), unique=True, nullable=False)
    password_hash = mapped_column(String(255), nullable=False)
    is_active = mapped_column(Boolean, nullable=False, server_default=text("true"), default=True)
    created_at = mapped_column(DateTime, nullable=False, server_default=text("now()"), default=datetime.now)