import React, { useState, useEffect } from "react";
import axios from "axios";

function MachinesPage() {
  const [machines, setMachines] = useState([]);

  useEffect(() => {
    axios
      .get("/api/machines/")
      .then((response) => {
        setMachines(response.data);
      })
      .catch((error) => {
        console.error("There was an error fetching the machines!", error);
      });
  }, []);

  return (
    <div>
      <h1>Machines</h1>
      <table>
        <thead>
          <tr>
            <th>Serial Number</th>
            <th>Model</th>
            <th>Engine Model</th>
            {/* Add other columns as needed */}
          </tr>
        </thead>
        <tbody>
          {machines.map((machine) => (
            <tr key={machine.id}>
              <td>{machine.serial_number}</td>
              <td>{machine.model}</td>
              <td>{machine.engine_model}</td>
              {/* Add other columns as needed */}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default MachinesPage;
