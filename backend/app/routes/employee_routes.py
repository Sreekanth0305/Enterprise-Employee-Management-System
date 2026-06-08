# from fastapi import APIRouter

# from app.controllers.employee_controller import (
#     get_all_employees,
#     get_employee_by_id
# )

# from app.utils.response_handler import (
#     success_response,
#     error_response
# )

# employee_router = APIRouter()

# @employee_router.get("/employees")
# def fetch_employees():

#     employees = get_all_employees()

#     return success_response(employees)

# @employee_router.get("/employees/{employee_id}")
# def fetch_employee(employee_id: int):

#     employee = get_employee_by_id(employee_id)

#     if "message" in employee:

#         return error_response(
#             "Not Found Employee"
#         )

#     return success_response(employee)

from fastapi import APIRouter

from app.models.employee_model import EmployeeSchema

from app.database.employee_db import (
    employees,
    save_employees,
    load_saved_employees
)

from datetime import datetime

from app.database.audit_logs_db import (
    audit_logs,
    save_audit_logs
)

from fastapi import Body

import json


employee_router = APIRouter()


def load_employees():

    global employees

    saved_employees = load_saved_employees()


    employees.clear()

    employees.extend(saved_employees)


@employee_router.get("/employees/{company_id}")
def get_employees(company_id: int):

    load_employees()

    filtered_employees = [

        employee

        for employee in employees

        if employee["company_id"] == company_id
    ]

    return filtered_employees

@employee_router.post("/employees")

def add_employee(employee: EmployeeSchema):

    load_employees()

    new_employee = {

    "id": len(employees) + 1,

    "name": employee.name,

    "email": employee.email,

    "department": employee.department,

    "role": employee.role,

    "status": employee.status,

    "attendance": 95,

    "company_id": employee.company_id
}

    employees.append(new_employee)

    save_employees(employees)

    audit_logs.append({
    "user_name": employee.performed_by,
    "company_id": new_employee["company_id"],
    "action": "Employee Created",
    "related_employee": new_employee["name"],
    "timestamp": str(datetime.now())
})
    
    save_audit_logs(audit_logs)

    return {

        "message":
        "Employee Added Successfully",

        "employee":
        new_employee
    }

@employee_router.put("/employees/{employee_id}")
def update_employee(
    employee_id: int,
    updated_employee: EmployeeSchema
):
    load_employees()

    for employee in employees:

        if employee["id"] == employee_id:

            employee["name"] = updated_employee.name

            employee["email"] = updated_employee.email

            employee["department"] = updated_employee.department

            employee["role"] = updated_employee.role

            employee["status"] = updated_employee.status

            employee["company_id"] = updated_employee.company_id

            save_employees(employees)

            audit_logs.append({
    "user_name": updated_employee.performed_by,
    "company_id": updated_employee.company_id,
    "action": "Employee Updated",
    "related_employee": updated_employee.name,
    "timestamp": str(datetime.now())
})
            
            save_audit_logs(audit_logs)       

            return {

                "message":
                "Employee Updated Successfully",
                "employee":
                employee
            }

    return {

        "message":
        "Employee Not Found"
    }
@employee_router.delete("/employees/{employee_id}")

def delete_employee(employee_id: int,
                    data: dict = Body(...)):

    for employee in employees:

        if employee["id"] == employee_id:

            employees.remove(employee)

            save_employees(employees)

            audit_logs.append({
    "user_name": data["performed_by"],
    "company_id": employee["company_id"],
    "action": "Employee Deleted",
    "related_employee": employee["name"],
    "timestamp": str(datetime.now())
})
            save_audit_logs(audit_logs)

            return {

                "message":
                "Employee Deleted Successfully"
            }

    return {

        "message":
        "Employee Not Found"
    }

@employee_router.get(
    "/attendance-report"
)
def attendance_report():

    report = []

    for employee in employees:

        report.append({

            "id":
            employee["id"],

            "name":
            employee["name"],

            "department":
            employee["department"],

            "attendance":
            employee["attendance"]
        })

    return report