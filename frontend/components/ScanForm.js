import React, { useState } from "react";
import api from "../services/api";

const ScanForm = () => {
  const [url, setUrl] = useState("");
  const [scanType, setScanType] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await api.post("/scan/run", { target_url: url, scan_type: scanType });
      alert(`Scan Result: ${response.data.result}`);
    } catch (err) {
      alert("Scan failed!");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" value={url} onChange={(e) => setUrl(e.target.value)} placeholder="Target URL" />
      <select value={scanType} onChange={(e) => setScanType(e.target.value)}>
        <option value="">Select Scan Type</option>
        <option value="sql_injection">SQL Injection</option>
        <option value="xss">XSS</option>
      </select>
      <button type="submit">Run Scan</button>
    </form>
  );
};

export default ScanForm;
