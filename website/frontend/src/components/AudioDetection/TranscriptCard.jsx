import React from "react";

export default function TranscriptCard({ transcript }) {
  if (!transcript) return null;

  return (
    <div className="transcript-card">
      <h2>📝 Speech Transcript</h2>

      <div className="transcript-content">{transcript}</div>
    </div>
  );
}
