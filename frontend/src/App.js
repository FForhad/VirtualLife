import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./pages/homepage/index.jsx";
import ServicePage from "./pages/servicepage/index.jsx";
import LoginPage from "./pages/loginpage/index.jsx";  // Import LoginPage

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/services" element={<ServicePage />} />
      </Routes>
    </Router>
  );
}

export default App;
