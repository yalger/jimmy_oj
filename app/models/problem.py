from sqlalchemy import Integer, String, Text, text
from sqlalchemy.orm import mapped_column
from app.db.base import Base


class Problem(Base):

    __tablename__ = "problems"

    id = mapped_column(Integer, primary_key=True, index=True)
    title = mapped_column(String(255), nullable=False, index=True)
    description = mapped_column(Text, nullable=False)
    time_limit = mapped_column(Integer, nullable=False, server_default=text("2"), default=2)