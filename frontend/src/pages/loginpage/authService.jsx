// src/services/authService.js
export const loginWithGoogle = async (accessToken) => {
    try {
        const response = await fetch(`${process.env.REACT_APP_API_URL}/auth/google-login/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ token: accessToken }),
        });

        if (!response.ok) {
            throw new Error("Failed to login");
        }

        return await response.json();
    } catch (error) {
        console.error("Login error:", error);
        return { error: error.message };
    }
};
