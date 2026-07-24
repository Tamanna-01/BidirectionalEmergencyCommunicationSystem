import { useEffect, useRef, useState } from "react";
import axios from "axios";

const API_URL = "http://127.0.0.1:8000/process-audio";
const HEALTH_URL = "http://127.0.0.1:8000/health";

const MAX_DURATION = 15;

export default function useAudioDetection() {
  const [monitoringActive, setMonitoringActive] = useState(false);
  const [loading, setLoading] = useState(false);
  const [backendConnected, setBackendConnected] = useState(false);

  const [elapsed, setElapsed] = useState(0);

  const [sound, setSound] = useState("");
  const [confidence, setConfidence] = useState(0);
  const [transcript, setTranscript] = useState("");
  const [simplifiedPhrase, setSimplifiedPhrase] = useState("");
  const [processingTime, setProcessingTime] = useState(null);
  const [isEmergency, setIsEmergency] = useState(false);

  const [history, setHistory] = useState([]);
  const [error, setError] = useState("");

  const mediaRecorderRef = useRef(null);
  const chunksRef = useRef([]);
  const streamRef = useRef(null);
  const timerRef = useRef(null);

  useEffect(() => {
    checkBackend();
  }, []);

  async function checkBackend() {
    try {
      await axios.get(HEALTH_URL);
      setBackendConnected(true);
    } catch {
      setBackendConnected(false);
    }
  }

  async function startMonitoring() {
    try {
      setError("");

      const stream = await navigator.mediaDevices.getUserMedia({
        audio: true,
      });

      streamRef.current = stream;

      const recorder = new MediaRecorder(stream);

      mediaRecorderRef.current = recorder;
      chunksRef.current = [];

      recorder.ondataavailable = (event) => {
        if (event.data.size > 0) {
          chunksRef.current.push(event.data);
        }
      };

      recorder.onstop = uploadRecording;

      recorder.start();

      setElapsed(0);
      setMonitoringActive(true);

      timerRef.current = setInterval(() => {
        setElapsed((prev) => {
          if (prev + 1 >= MAX_DURATION) {
            stopMonitoring();
            return MAX_DURATION;
          }
          return prev + 1;
        });
      }, 1000);
    } catch {
      setError("Unable to access microphone.");
    }
  }

  function stopMonitoring() {
    clearInterval(timerRef.current);

    setMonitoringActive(false);

    if (
      mediaRecorderRef.current &&
      mediaRecorderRef.current.state !== "inactive"
    ) {
      mediaRecorderRef.current.stop();
    }

    if (streamRef.current) {
      streamRef.current.getTracks().forEach((track) => track.stop());
    }
  }

  async function uploadRecording() {
    try {
      setLoading(true);

      const blob = new Blob(chunksRef.current, {
        type: "audio/wav",
      });

      const formData = new FormData();
      formData.append("file", blob, "recording.wav");

      const response = await axios.post(API_URL, formData);

      const data = response.data;

      setSound(data.sound || "");
      setConfidence(data.confidence || 0);
      setTranscript(data.transcript || "");
      setSimplifiedPhrase(data.simplified_text || "");
      setProcessingTime(data.processing_time_ms || null);
      setIsEmergency(data.is_emergency || false);

      const item = {
        id: Date.now(),
        timestamp: new Date().toLocaleTimeString(),
        sound: data.sound,
        confidence: data.confidence,
        transcript: data.transcript,
        simplifiedPhrase: data.simplified_text,
        processingTime: data.processing_time_ms,
        isEmergency: data.is_emergency,
      };

      setHistory((prev) => [item, ...prev].slice(0, 3));
    } catch {
      setError("Audio analysis failed.");
    } finally {
      setLoading(false);
    }
  }

  function selectHistoryItem(item) {
    setSound(item.sound);
    setConfidence(item.confidence);
    setTranscript(item.transcript);
    setSimplifiedPhrase(item.simplifiedPhrase);
    setProcessingTime(item.processingTime);
    setIsEmergency(item.isEmergency);
  }

  const progress = (elapsed / MAX_DURATION) * 100;

  return {
    monitoringActive,
    loading,
    backendConnected,

    formattedElapsedTime: `00:${String(elapsed).padStart(2, "0")}`,
    formattedRemainingTime: `00:${String(MAX_DURATION - elapsed).padStart(
      2,
      "0",
    )}`,

    progress,

    sound,
    confidence,
    transcript,
    simplifiedPhrase,
    processingTime,
    isEmergency,

    history,
    error,

    startMonitoring,
    stopMonitoring,
    selectHistoryItem,
  };
}
