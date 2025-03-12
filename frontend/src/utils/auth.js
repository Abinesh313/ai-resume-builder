import { api } from "./api";

export const loginUser = async (data) => {
  try {
    const response = await api.post("/login", data);
    return response.data;
  } catch (error) {
    console.error("Login Error:", error);
  }
};
