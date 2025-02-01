import axios from "axios";

// Base URL for the API
const API_BASE_URL = "http://127.0.0.1:8000";

// Login API function
export const loginUser = async (identifier, password) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/api/users/login`, {
      identifier,
      password,
    });
    return response.data; // Return response data
  } catch (error) {
    throw error.response?.data?.message || "Login failed. Please try again.";
  }
};

// Register API function
export const registerUser = async (name, email, password) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/api/users/register`, {
      name,
      email,
      password,
    });
    return response.data; // Return response data
  } catch (error) {
    throw error.response?.data?.message || "Registration failed. Please try again.";
  }
};

// Forgot Password API function
export const forgotPassword = async (email) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/api/users/forgot-password`, {
      email,
    });
    return response.data; // Return response data
  } catch (error) {
    throw error.response?.data?.message || "Failed to send reset link. Please try again.";
  }
};

// Add more API functions here (e.g., getUserProfile, etc.)
