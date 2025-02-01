import React, { useState } from "react";
import "./login.css";
import InputField from "../../components/InputField";
import Button from "../../components/Button";
import { loginUser } from "../../utils/api"; // Import API functions
import GoogleLoginButton from "../../components/GoogleLoginButton"; // Import Google button component

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  // Handle normal login
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const data = await loginUser(email, password);
      console.log("Login successful:", data);
      localStorage.setItem("token", data.token); // Store token if needed
    } catch (error) {
      console.error("Login failed:", error);
      alert(error);
    }
  };

  return (
    <div className="login-container">
      <div className="login-box">
        <h2>Login</h2>
        <form onSubmit={handleSubmit}>
          <InputField label="Email" type="email" value={email} onChange={setEmail} />
          <InputField label="Password" type="password" value={password} onChange={setPassword} />
          <Button text="Login" />
        </form>

        {/* Register & Forgot Password Links */}
        <div className="auth-links">
          <a href="/register">Create an account</a>
          <a href="/forgot-password">Forgot password?</a>
        </div>

        {/* ✅ Render Google Login Button Correctly */}
        <GoogleLoginButton />
      </div>
    </div>
  );
};

export default Login;
