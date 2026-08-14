import React, { useState, useEffect } from "react";

import MonitoringCard from "../../components/AudioDetection/MonitoringCard";
import DetectionResultCard from "../../components/AudioDetection/DetectionResultCard";
import TranscriptCard from "../../components/AudioDetection/TranscriptCard";
import SimplifiedPhraseCard from "../../components/AudioDetection/SimplifiedPhraseCard";

import useAudioDetection from "../../hooks/useAudioDetection";

import "./AudioDetection.css";

export default function AudioDetection() {
  const {
    monitoringActive,
    loading,
    backendConnected,

    formattedElapsedTime,
    formattedRemainingTime,
    progress,

    sound,
    confidence,
    transcript,
    simplifiedPhrase,
    processingTime,
    isEmergency,

    history,
    selectHistoryItem,

    error,

    startMonitoring,
    stopMonitoring,
  } = useAudioDetection();

  // State to manage the popup visibility
  const [showPopup, setShowPopup] = useState(false);

  // Trigger the popup to appear whenever an emergency is detected
  useEffect(() => {
    if (isEmergency) {
      setShowPopup(true);
    } else {
      setShowPopup(false);
    }
  }, [isEmergency]);

  // Determine if there is any data to display in the right panel
  const hasOutput = sound || transcript || simplifiedPhrase || history.length > 0 || error;

  return (
    <div className={`audio-page ${hasOutput ? "has-output" : "initial-state"}`}>
      
      <div className="left-panel">
        <MonitoringCard
          monitoringActive={monitoringActive}
          loading={loading}
          backendConnected={backendConnected}
          formattedElapsedTime={formattedElapsedTime}
          formattedRemainingTime={formattedRemainingTime}
          progress={progress}
          startMonitoring={startMonitoring}
          stopMonitoring={stopMonitoring}
        />

        {(sound || transcript || simplifiedPhrase) && (
          <div className={`emergency-banner ${isEmergency ? "danger" : "safe"}`}>
            {isEmergency ? "🚨 EMERGENCY DETECTED" : "✅ No Emergency Detected"}
          </div>
        )}

        {/* Moved Simplified Phrase below the banner in the left panel */}
        {isEmergency && simplifiedPhrase && (
          <SimplifiedPhraseCard simplifiedPhrase={simplifiedPhrase} />
        )}

        {error && <div className="error-card">{error}</div>}
      </div>

      <div className="right-panel">
        <DetectionResultCard
          sound={sound}
          confidence={confidence}
          processingTime={processingTime}
        />

        <TranscriptCard transcript={transcript} />

        {/* Recent Analyses moves up naturally since SimplifiedPhraseCard was relocated */}
        {history.length > 0 && (
          <div className="history-section">
            <h2>Recent Analyses</h2>

            <div className="history-list">
              {history.map((item) => (
                <div
                  key={item.id}
                  className="history-card"
                  onClick={() => selectHistoryItem(item)}
                >
                  <div className="history-header">
                    <span>{item.timestamp}</span>

                    <span
                      className={`history-status ${
                        item.isEmergency ? "danger" : "safe"
                      }`}
                    >
                      {item.isEmergency ? "Emergency" : "Safe"}
                    </span>
                  </div>

                  <div className="history-sound">{item.sound}</div>

                  <div className="history-confidence">
                    Confidence: {Number(item.confidence).toFixed(2)}%
                  </div>

                  <div className="history-phrase">{item.simplifiedPhrase}</div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>

      {/* Global Emergency Popup Overlay (Centered with Close Button) */}
      {showPopup && (
        <div className="emergency-popup-overlay">
          <div className="emergency-popup">
            <button 
              className="popup-close-btn" 
              onClick={() => setShowPopup(false)}
              aria-label="Close alert"
            >
              ✕
            </button>
            <span className="popup-icon">🚨</span>
            <div className="popup-text">
              <div className="popup-title">EMERGENCY DETECTED</div>
              <div className="popup-subtitle">Immediate attention required based on audio analysis</div>
            </div>
          </div>
        </div>
      )}

    </div>
  );
}