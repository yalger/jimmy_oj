from sqlalchemy import Integer, ForeignKey, Text, null
from sqlalchemy.orm import mapped_column
from app.db.base import Base


class Testcase(Base):

    __tablename__ = "testcases"

    id = mapped_column(Integer, primary_key=True, index=True)

    problem_id = mapped_column(
        Integer,
        ForeignKey("problems.id")
    )

    tc_num = mapped_column(Integer, nullable=False)
    input_data = mapped_column(Text)
    output_data = mapped_column(Text)