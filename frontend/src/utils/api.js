import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000";

export const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// Example API call
export const testBackend = async () => {
  try {
    const response = await api.get("/");
    return response.data;
  } catch (error) {
    console.error("Backend Error:", error);
    return null;
  }
};
