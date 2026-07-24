import React from "react";

export default function MonitoringCard({
  monitoringActive,
  loading,
  backendConnected,

  formattedElapsedTime,
  formattedRemainingTime,
  progress,

  startMonitoring,
  stopMonitoring,
}) {
  return (
    <div className="monitoring-card">
      <h2>🎙 Audio Monitoring</h2>

      <div
        className={`backend-status ${backendConnected ? "online" : "offline"}`}
      >
        {backendConnected ? "🟢 Backend Connected" : "🔴 Backend Offline"}
      </div>

      <div className="recording-info">
        <strong>Maximum Recording Duration:</strong>
        <br />
        15 seconds
        <br />
        <br />
        Recording automatically stops after 15 seconds and is sent for AI
        analysis.
      </div>

      {!monitoringActive && !loading && (
        <button
          className="start-btn"
          onClick={startMonitoring}
          disabled={!backendConnected}
        >
          🎙 Start Listening
        </button>
      )}

      {monitoringActive && (
        <div className="recording-section">
          <div className="recording-status">🔴 Listening...</div>

          <div className="timer">
            {formattedElapsedTime}
            {" / "}
            {formattedRemainingTime}
          </div>

          <div className="progress-container">
            <div
              className="progress-fill"
              style={{
                width: `${progress}%`,
              }}
            />
          </div>

          <button className="stop-btn" onClick={stopMonitoring}>
            ⏹ Stop & Analyze
          </button>
        </div>
      )}

      {loading && (
        <div className="processing">
          <div className="spinner" />

          <h3>Processing Audio...</h3>

          <ul>
            <li>✔ Uploading recording</li>
            <li>✔ Detecting emergency sound</li>
            <li>✔ Speech recognition</li>
            <li>✔ Simplifying emergency phrase</li>
          </ul>
        </div>
      )}
    </div>
  );
}
