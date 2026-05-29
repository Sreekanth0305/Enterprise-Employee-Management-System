// import axios from "axios";

// const API_URL =
//   "http://127.0.0.1:8001";

// export const getEmployees =
//   async () => {

//     const response =
//       await axios.get(
//         `${API_URL}/employees`
//       );

//     return response.data.data;
//   };

// export const addEmployee =
//   async (employeeData) => {

//     const response =
//       await axios.post(
//         `${API_URL}/employees`,
//         employeeData
//       );

//     return response.data.data;
//   };

import axios from "axios";

const API_URL =
  "http://127.0.0.1:8001";

// GET EMPLOYEES

export const getEmployees =
  async () => {

    // CHECK LOCAL STORAGE FIRST

    const localEmployees =
      JSON.parse(
        localStorage.getItem(
          "employees"
        )
      );

    if (
      localEmployees &&
      localEmployees.length > 0
    ) {

      return localEmployees;
    }

    // FETCH FROM BACKEND

    const response =
      await axios.get(
        `${API_URL}/employees`
      );

    // SAVE TO LOCAL STORAGE

    localStorage.setItem(

      "employees",

      JSON.stringify(
        response.data
      )
    );

    return response.data;
  };

// ADD EMPLOYEE

export const addEmployee =
  async (employeeData) => {

    const response =
      await axios.post(

        `${API_URL}/employees`,

        employeeData
      );

    const employees =
      JSON.parse(
        localStorage.getItem(
          "employees"
        )
      ) || [];

    employees.push(
      response.data.employee
    );

    localStorage.setItem(

      "employees",

      JSON.stringify(
        employees
      )
    );

    return response.data;
  };

// UPDATE EMPLOYEE

export const updateEmployee =
  async (
    id,
    employeeData
  ) => {

    const response =
      await axios.put(

        `${API_URL}/employees/${id}`,

        employeeData
      );

    let employees =
      JSON.parse(
        localStorage.getItem(
          "employees"
        )
      ) || [];

    employees = employees.map(
      (employee) =>

        employee.id === id

          ? {
              ...employee,
              ...employeeData
            }

          : employee
    );

    localStorage.setItem(

      "employees",

      JSON.stringify(
        employees
      )
    );

    return response.data;
  };

// DELETE EMPLOYEE

export const deleteEmployee =
  async (id) => {

    const response =
      await axios.delete(

        `${API_URL}/employees/${id}`
      );

    let employees =
      JSON.parse(
        localStorage.getItem(
          "employees"
        )
      ) || [];

    employees = employees.filter(
      employee =>
        employee.id !== id
    );

    localStorage.setItem(

      "employees",

      JSON.stringify(
        employees
      )
    );

    return response.data;
  };