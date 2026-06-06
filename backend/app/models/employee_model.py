from pydantic import BaseModel

class EmployeeSchema(BaseModel):

    name: str

    email: str

    department: str

    role: str

    status: str = "Active"

    company_id: int