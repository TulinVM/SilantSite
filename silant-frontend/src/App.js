import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import HomePage from "./pages/HomePage";
import MachinesPage from "./pages/MachinesPage";
import MaintenancePage from "./pages/MaintenancePage";
import ComplaintsPage from "./pages/ComplaintsPage";
import LoginPage from "./pages/LoginPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" exact component={HomePage} />
        <Route path="/machines" component={MachinesPage} />
        <Route path="/maintenance" component={MaintenancePage} />
        <Route path="/complaints" component={ComplaintsPage} />
        <Route path="/login" component={LoginPage} />
      </Routes>
    </Router>
  );
}

export default App;
