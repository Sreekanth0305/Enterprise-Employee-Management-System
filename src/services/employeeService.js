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

    const currentUser =
      JSON.parse(
        localStorage.getItem(
          "authUser"
        )
      );

    const response =
      await axios.get(
        `${API_URL}/employees/${currentUser.company_id}`
      );

    return response.data;
  };
    

// ADD EMPLOYEE

export const addEmployee =
  async (employeeData) => {

    const currentUser =
      JSON.parse(
        localStorage.getItem(
          "authUser"
        )
      );

    employeeData.company_id =
      currentUser.company_id;

    const response =
      await axios.post(
        `${API_URL}/employees`,
        employeeData
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

       
    return response.data;
  };

// DELETE EMPLOYEE

export const deleteEmployee =
  async (
    id,
    performed_by
  ) => {

    const response =
      await axios.delete(
        `${API_URL}/employees/${id}`,
        {
          data: {
            performed_by
          }
        }
      );

    return response.data;
  };

  export const updateEmployeeStatus =
async (
  employeeId,
  status
) => {

  const response =
    await axios.put(

      `${API_URL}/employees/${employeeId}/status`,

      {
        status
      }
    );

  return response.data;
};