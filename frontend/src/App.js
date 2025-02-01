import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { GoogleOAuthProvider } from "@react-oauth/google";
import HomePage from "./pages/homepage/index.jsx";
import ServicePage from "./pages/servicepage/index.jsx";
import LoginPage from "./pages/loginpage/index.jsx";  // Import LoginPage

const clientId = process.env.REACT_APP_GOOGLE_OAUTH2_CLIENT_ID

function App() {
  return (
    <GoogleOAuthProvider clientId={clientId}>
      <Router>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/services" element={<ServicePage />} />
        </Routes>
      </Router>
    </GoogleOAuthProvider>
  );
}

export default App;
