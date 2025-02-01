import React, { useState } from "react";
import { forgotPassword } from "../../utils/api";

const ForgotPasswordPage = () => {
  const [email, setEmail] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const data = await forgotPassword(email);
      console.log("Reset link sent:", data);
      // Show success message
    } catch (error) {
      console.error("Failed to send reset link:", error);
      alert(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
      <button type="submit">Send Reset Link</button>
    </form>
  );
};

export default ForgotPasswordPage;
