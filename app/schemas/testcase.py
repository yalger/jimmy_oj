from pydantic import BaseModel

class AddTestcaseRequest(BaseModel):
    problem_id: int
    input_data: str
    output_data: str