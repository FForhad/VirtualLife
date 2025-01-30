import React from "react";
import { useGoogleLogin } from "@react-oauth/google";

const apiUrl = process.env.REACT_APP_API_URL;

const GoogleLoginButton = () => {
    const login = useGoogleLogin({
        onSuccess: (response) => {
            if (!response.access_token) {
                console.error("Access Token is missing!");
                return;
            }

            // Get the API URL from the .env file
            const Url = `${apiUrl}auth/google-login/`

            // Send the access token to the backend
            fetch(Url, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ token: response.access_token }), // Send access token
            })
                .then((res) => res.json())
                .then((data) => {
                    console.log("Backend Response:", data);
                    // Optionally, handle login success (redirect, etc.)
                })
                .catch((error) => {
                    console.error("Error:", error);
                });
        },
        onError: (error) => {
            console.log("Login Failed:", error);
        },
    });

    return (
        <button
            onClick={() => login()} // When button is clicked, it triggers login
            style={{
                padding: "10px 20px",
                background: "#4285F4",
                color: "#fff",
                border: "none",
                borderRadius: "5px",
                cursor: "pointer",
                fontSize: "16px",
                marginTop: "10px",
            }}>
            Sign in with Google
        </button>
    );
};

export default GoogleLoginButton;
