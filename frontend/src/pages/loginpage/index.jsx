import React from "react";
import { GoogleOAuthProvider } from "@react-oauth/google";
import GoogleLoginButton from "../../components/GoogleLoginButton";
import LoginForm from "../../components/LoginForm";
import styles from "./login.css";
import { Link } from "react-router-dom";

const CLIENT_ID = process.env.REACT_APP_GOOGLE_OAUTH2_CLIENT_ID;

const LoginPage = () => {
    const handleGoogleLogin = (userData) => {
        console.log("Google Login Success:", userData);
        localStorage.setItem("user", JSON.stringify(userData));
    };

    const handleFormSubmit = (formData) => {
        console.log("Email Login:", formData);
    };

    return (
        <GoogleOAuthProvider clientId={CLIENT_ID}>
            <div className={styles.container}>
                <div className={styles.loginBox}>
                    <h2 className={styles.title}>Login</h2>
                    <LoginForm onSubmit={handleFormSubmit} />

                    <div className={styles.footerLinks}>
                        <Link to="/forgot-password" className={styles.link}>Forgot Password?</Link>
                        <span className={styles.separator}>|</span>
                        <Link to="/register" className={styles.link}>Create an Account</Link>
                    </div>
                    
                    <div className={styles.orDivider}>or</div>
                    <GoogleLoginButton onLoginSuccess={handleGoogleLogin} />
                </div>
            </div>
        </GoogleOAuthProvider>
    );
};

export default LoginPage;
