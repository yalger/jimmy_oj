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

    code = mapped_column(Text)

    status = mapped_column(
        String(50),
        server_default=text("'Pending'"),
        default="Pending"
    )

    result = mapped_column(Text)