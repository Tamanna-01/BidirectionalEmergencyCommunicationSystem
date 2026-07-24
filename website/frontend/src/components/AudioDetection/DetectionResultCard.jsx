import React from "react";

export default function DetectionResultCard({
  sound,
  confidence,
  processingTime,
}) {
  if (!sound) return null;

  return (
    <div className="result-card">
      <h2>🔊 AI Detection Result</h2>

      <div className="result-grid">
        <div className="result-item">
          <span className="label">Detected Sound</span>
          <span className="value">{sound}</span>
        </div>

        <div className="result-item">
          <span className="label">Confidence</span>
          <span className="value">{Number(confidence || 0).toFixed(2)}%</span>
        </div>

        <div className="result-item full-width">
          <span className="label">Processing Time</span>
          <span className="value">
            {processingTime ? `${processingTime} ms` : "--"}
          </span>
        </div>
      </div>
    </div>
  );
}
