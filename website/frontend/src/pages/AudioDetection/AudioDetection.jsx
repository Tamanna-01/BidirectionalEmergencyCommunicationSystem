import React from "react";

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

  return (
    <div className="audio-page">
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

        {error && <div className="error-card">{error}</div>}
      </div>

      <div className="right-panel">
        {(sound || transcript || simplifiedPhrase) && (
          <div
            className={`emergency-banner ${isEmergency ? "danger" : "safe"}`}
          >
            {isEmergency ? "🚨 Emergency Detected" : "✅ No Emergency Detected"}
          </div>
        )}

        <DetectionResultCard
          sound={sound}
          confidence={confidence}
          processingTime={processingTime}
        />

        <TranscriptCard transcript={transcript} />

        <SimplifiedPhraseCard simplifiedPhrase={simplifiedPhrase} />

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
    </div>
  );
}
