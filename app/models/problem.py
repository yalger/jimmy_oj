from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import mapped_column
from app.db.base import Base


class Problem(Base):

    __tablename__ = "problems"

    id = mapped_column(Integer, primary_key=True, index=True)
    title = mapped_column(String(255), nullable=False, index=True)
    description = mapped_column(Text, nullable=False)
    data_path = mapped_column(String)