import { Button } from "antd";
import "../src/styles/app.css"
import HomePage from "./pages/homepage";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import ServicePage from "./pages/servicepage";
function App() {
  return (
    <div>
      <Router><HomePage/><ServicePage/></Router>
      

    </div>
  );
}

export default App;
