from unittest import expectedFailure

from sqlalchemy import Integer, Text, ForeignKey, String, text
from sqlalchemy.orm import mapped_column
from app.db.base import Base


class Submission(Base):

    __tablename__ = "submissions"

    id = mapped_column(Integer, primary_key=True, index=True)

    user_id = mapped_column(
        Integer,
        ForeignKey("users.id")
    )

    problem_id = mapped_column(
        Integer,
        ForeignKey("problems.id")
    )

    language = mapped_column(String(10))
    code = mapped_column(Text)

    status = mapped_column(
        String(50),
        server_default=text("'Pending'"),
        default="Pending"
    )

    time_used = mapped_column(Integer)
    memory_used = mapped_column(Integer)

    wrong_tc_id = mapped_column(
        Integer,
        ForeignKey("testcases.id"),
    )

    wrong_output = mapped_column(Text)