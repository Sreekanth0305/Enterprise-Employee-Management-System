employees = []

import json

FILE_NAME = "app/database/employees.json"

def save_employees(employees):

    with open(FILE_NAME, "w") as file:

        json.dump(
            employees,
            file,
            indent=4
        )

def load_saved_employees():

    try:

        with open(FILE_NAME, "r") as file:

            return json.load(file)

    except:

        return []