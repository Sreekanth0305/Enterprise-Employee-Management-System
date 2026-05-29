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

from app.database.employee_db import employees

import requests

employee_router = APIRouter()

API_URL = "https://jsonplaceholder.typicode.com/users"

def load_employees():

    # Prevent duplicate loading

    global employees

    if employees:
        return

    response = requests.get(API_URL)

    data = response.json()

    employees.clear()

    for index, user in enumerate(data):

        employees.append({

            "id": user["id"],

            "name": user["name"],

            "email": user["email"],

            "department":
                "IT"
                if index % 4 == 0
                else "HR"
                if index % 4 == 1
                else "Finance"
                if index % 4 == 2
                else "Design",

            "role":
                "Frontend Developer"
                if index % 2 == 0
                else "Backend Developer",

            "status":
                "Active"
                if index % 3 != 0
                else "Inactive",

            "attendance":
                90 - index
        })

@employee_router.get("/employees")

def get_employees():

    load_employees()

    return employees

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

        "attendance": 95
    }

    employees.append(new_employee)

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

    for employee in employees:

        if employee["id"] == employee_id:

            employee["name"] = updated_employee.name

            employee["email"] = updated_employee.email

            employee["department"] = updated_employee.department

            employee["role"] = updated_employee.role

            employee["status"] = updated_employee.status

            return {

                "message":
                "Employee Updated Successfully"
            }

    return {

        "message":
        "Employee Not Found"
    }

@employee_router.delete("/employees/{employee_id}")

def delete_employee(employee_id: int):

    for employee in employees:

        if employee["id"] == employee_id:

            employees.remove(employee)

            return {

                "message":
                "Employee Deleted Successfully"
            }

    return {

        "message":
        "Employee Not Found"
    }