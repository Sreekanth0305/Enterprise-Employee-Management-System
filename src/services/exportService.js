import axios from "axios";

const API_URL =
  "http://127.0.0.1:8001";

export const logExport =
(data) =>

axios.post(
`${API_URL}/exports/log`,
data
);

export const getExportHistory =
(companyId) =>

axios.get(
`${API_URL}/exports/history/${companyId}`
);