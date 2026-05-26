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
  "https://jsonplaceholder.typicode.com/users";

/* GET EMPLOYEES */

export const getEmployees =
  async () => {

    const response =
      await axios.get(API_URL);

    return response.data.map(
      (employee, index) => ({

        id: employee.id,

        name: employee.name,

        email: employee.email,

        department:
          index % 4 === 0
            ? "IT"
            : index % 4 === 1
            ? "HR"
            : index % 4 === 2
            ? "Finance"
            : "Design",

        role:
          index % 2 === 0
            ? "Frontend Developer"
            : "Backend Developer",

        status:
          index % 2 === 0
            ? "Active"
            : "Inactive",
      })
    );
  };

/* ADD EMPLOYEE */

export const addEmployee =
  async (employeeData) => {

    const response =
      await axios.post(
        API_URL,
        employeeData
      );

    return response.data;
  };

/* UPDATE EMPLOYEE */

export const updateEmployee =
  async (
    employeeId,
    employeeData
  ) => {

    const response =
      await axios.put(
        `${API_URL}/${employeeId}`,
        employeeData
      );

    return response.data;
  };

/* DELETE EMPLOYEE */

export const deleteEmployee =
  async (employeeId) => {

    const response =
      await axios.delete(
        `${API_URL}/${employeeId}`
      );

    return response.data;
  };