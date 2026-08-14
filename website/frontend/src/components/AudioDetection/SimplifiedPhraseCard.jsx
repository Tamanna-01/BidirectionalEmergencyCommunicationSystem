import React from "react";

export default function SimplifiedPhraseCard({ simplifiedPhrase }) {
  if (!simplifiedPhrase) return null;

  return (
    <div className="simplified-card">
      <h2>🚨 Simplified Emergency Phrase</h2>

      <div className="simplified-content">{simplifiedPhrase}</div>
    </div>
  );
}
