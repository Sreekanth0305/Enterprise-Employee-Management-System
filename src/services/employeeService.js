import axios from "axios";

const API_URL =
  "http://127.0.0.1:8001";

export const getEmployees =
  async () => {

    const response =
      await axios.get(
        `${API_URL}/employees`
      );

    return response.data.data;
  };

export const addEmployee =
  async (employeeData) => {

    const response =
      await axios.post(
        `${API_URL}/employees`,
        employeeData
      );

    return response.data.data;
  };