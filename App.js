import React, { useState } from 'react';
import './App.css';

function App() {
  const [confirmed, setConfirmed] = useState('');
  const [deaths, setDeaths] = useState('');
  const [recovered, setRecovered] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Simple calculation to predict recovered cases (This is just a placeholder and not a real ML model)
    const predictedRecovered = parseInt(confirmed, 10) - parseInt(deaths, 10);
    setRecovered(predictedRecovered);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>COVID-19 Recovery Prediction</h1>
        <form onSubmit={handleSubmit}>
          <div className="input-group">
            <label htmlFor="confirmed">Confirmed Cases:</label>
            <input
              type="number"
              id="confirmed"
              value={confirmed}
              onChange={(e) => setConfirmed(e.target.value)}
              required
            />
          </div>
          <div className="input-group">
            <label htmlFor="deaths">Deaths:</label>
            <input
              type="number"
              id="deaths"
              value={deaths}
              onChange={(e) => setDeaths(e.target.value)}
              required
            />
          </div>
          <button type="submit">Predict Recovered Cases</button>
        </form>
        {recovered && <p>Predicted Recovered Cases: {recovered}</p>}
      </header>
    </div>
  );
}

export default App;
