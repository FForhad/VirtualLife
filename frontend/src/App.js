import { GoogleOAuthProvider } from "@react-oauth/google";
import GoogleLoginButton from "./components/GoogleLoginButton";
import { BrowserRouter as Router } from "react-router-dom";
import HomePage from "./pages/homepage";
import ServicePage from "./pages/servicepage";

const CLIENT_ID = process.env.REACT_APP_GOOGLE_OAUTH2_CLIENT_ID; // Replace with your actual Client ID
console.log(CLIENT_ID);

function App() {
  return (
    <GoogleOAuthProvider clientId={CLIENT_ID}>
      <Router>
        <HomePage />
        {/* <ServicePage /> */}

        {/* Add the Google login button here */}
        <div style={{ textAlign: "center", marginTop: "20px" }}>
          <GoogleLoginButton />
        </div>
      </Router>
    </GoogleOAuthProvider>
  );
}

export default App;
