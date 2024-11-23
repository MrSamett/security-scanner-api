import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./components/Login";
import ScanForm from "./components/ScanForm";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/scan" element={<ScanForm />} />
      </Routes>
    </Router>
  );
}

export default App;
