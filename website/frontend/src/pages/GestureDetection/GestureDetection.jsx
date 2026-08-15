import { useEffect, useRef, useState } from "react";

import {
  Alert,
  Box,
  Button,
  Card,
  CardContent,
  CircularProgress,
  Divider,
  LinearProgress,
  Stack,
  Typography,
} from "@mui/material";

import { CameraAlt, Stop, VolumeUp, Replay } from "@mui/icons-material";

import { processGesture } from "../../services/api";

import "./GestureDetection.css";

const gestureMessages = {
  HELP: "I need help immediately.",
  CALL_AMBULANCE: "Please call an ambulance.",
  FIRE: "There is a fire.",
  CALL_DOCTOR: "I need a doctor.",
  STOP_DANGER: "Stop, there is danger.",
};

const RECORDING_DURATION = 3000;

function GestureDetection() {
  const videoRef = useRef(null);
  const streamRef = useRef(null);
  const mediaRecorderRef = useRef(null);

  const chunksRef = useRef([]);

  const timerRef = useRef(null);
  const stopTimeoutRef = useRef(null);

  const [cameraActive, setCameraActive] = useState(false);

  const [recording, setRecording] = useState(false);

  const [processing, setProcessing] = useState(false);

  const [result, setResult] = useState(null);

  const [error, setError] = useState("");

  const [remainingTime, setRemainingTime] = useState(0);

  // ==========================================================
  // Attach stream to video AFTER video element exists
  // ==========================================================

  useEffect(() => {
    if (cameraActive && videoRef.current && streamRef.current) {
      videoRef.current.srcObject = streamRef.current;

      videoRef.current.play().catch((err) => {
        console.error("Video playback error:", err);
      });
    }
  }, [cameraActive]);

  // ==========================================================
  // Start Camera
  // ==========================================================

  const startCamera = async () => {
    try {
      setError("");

      const stream = await navigator.mediaDevices.getUserMedia({
        video: {
          width: {
            ideal: 1280,
          },

          height: {
            ideal: 720,
          },

          facingMode: "user",
        },

        audio: false,
      });

      streamRef.current = stream;

      setCameraActive(true);
    } catch (err) {
      console.error(err);

      setError(
        "Unable to access the camera. Please allow camera permission and try again.",
      );
    }
  };

  // ==========================================================
  // Stop Camera
  // ==========================================================

  const stopCamera = () => {
    if (streamRef.current) {
      streamRef.current.getTracks().forEach((track) => {
        track.stop();
      });

      streamRef.current = null;
    }

    if (videoRef.current) {
      videoRef.current.srcObject = null;
    }

    setCameraActive(false);
  };

  // ==========================================================
  // Start Recording
  // ==========================================================

  const startRecording = () => {
    if (!streamRef.current || recording || processing) {
      return;
    }

    try {
      setError("");
      setResult(null);

      chunksRef.current = [];

      const supportedMimeTypes = ["video/webm;codecs=vp8", "video/webm"];

      const mimeType = supportedMimeTypes.find((type) =>
        MediaRecorder.isTypeSupported(type),
      );

      const recorder = mimeType
        ? new MediaRecorder(streamRef.current, {
            mimeType,
          })
        : new MediaRecorder(streamRef.current);

      mediaRecorderRef.current = recorder;

      recorder.ondataavailable = (event) => {
        if (event.data && event.data.size > 0) {
          chunksRef.current.push(event.data);
        }
      };

      recorder.onstop = async () => {
        const blobType = recorder.mimeType || "video/webm";

        const videoBlob = new Blob(chunksRef.current, {
          type: blobType,
        });

        await submitGesture(videoBlob);
      };

      recorder.start();

      setRecording(true);

      setRemainingTime(RECORDING_DURATION / 1000);

      const startTime = Date.now();

      timerRef.current = setInterval(() => {
        const elapsed = Date.now() - startTime;

        const remaining = Math.max(0, RECORDING_DURATION - elapsed);

        setRemainingTime(Math.ceil(remaining / 1000));
      }, 100);

      stopTimeoutRef.current = setTimeout(() => {
        stopRecording();
      }, RECORDING_DURATION);
    } catch (err) {
      console.error(err);

      setError("Unable to start gesture recording.");

      setRecording(false);
    }
  };

  // ==========================================================
  // Stop Recording
  // ==========================================================

  const stopRecording = () => {
    if (stopTimeoutRef.current) {
      clearTimeout(stopTimeoutRef.current);

      stopTimeoutRef.current = null;
    }

    if (timerRef.current) {
      clearInterval(timerRef.current);

      timerRef.current = null;
    }

    if (
      mediaRecorderRef.current &&
      mediaRecorderRef.current.state !== "inactive"
    ) {
      mediaRecorderRef.current.stop();
    }

    setRecording(false);

    setRemainingTime(0);
  };

  // ==========================================================
  // Send Video to Backend
  // ==========================================================

  const submitGesture = async (videoBlob) => {
    try {
      setProcessing(true);

      setError("");

      const data = await processGesture(videoBlob);

      setResult(data);
    } catch (err) {
      console.error(err);

      setError(
        err?.response?.data?.detail ||
          err?.message ||
          "Gesture detection failed.",
      );
    } finally {
      setProcessing(false);
    }
  };

  // ==========================================================
  // Speak Result
  // ==========================================================

  const speakGesture = () => {
    if (!result || !result.gesture || result.gesture === "UNKNOWN") {
      return;
    }

    const message = gestureMessages[result.gesture];

    if (!message) {
      return;
    }

    window.speechSynthesis.cancel();

    const utterance = new SpeechSynthesisUtterance(message);

    utterance.rate = 0.95;
    utterance.pitch = 1;
    utterance.volume = 1;

    window.speechSynthesis.speak(utterance);
  };

  // ==========================================================
  // Cleanup
  // ==========================================================

  useEffect(() => {
    return () => {
      if (timerRef.current) {
        clearInterval(timerRef.current);
      }

      if (stopTimeoutRef.current) {
        clearTimeout(stopTimeoutRef.current);
      }

      if (
        mediaRecorderRef.current &&
        mediaRecorderRef.current.state !== "inactive"
      ) {
        mediaRecorderRef.current.stop();
      }

      if (streamRef.current) {
        streamRef.current.getTracks().forEach((track) => track.stop());
      }

      window.speechSynthesis.cancel();
    };
  }, []);

  // ==========================================================
  // Display message
  // ==========================================================

  const displayMessage =
    result?.gesture && gestureMessages[result.gesture]
      ? gestureMessages[result.gesture]
      : "";

  return (
    <Box className="gesture-page">
      {/* =====================================================
          HEADER
      ====================================================== */}

      <Box className="gesture-header">
        <Box>
          <Typography className="gesture-eyebrow">
            USER-TO-ENVIRONMENT
          </Typography>

          <Typography variant="h4" className="gesture-title">
            Gesture Recognition
          </Typography>

          <Typography className="gesture-subtitle">
            Communicate emergency needs using Indian Sign Language.
          </Typography>
        </Box>

        <Box className="gesture-status">
          <span className={cameraActive ? "status-dot active" : "status-dot"} />

          <Typography>
            {cameraActive ? "Camera Ready" : "Camera Off"}
          </Typography>
        </Box>
      </Box>

      {/* =====================================================
          ERROR
      ====================================================== */}

      {error && (
        <Alert
          severity="error"
          className="gesture-alert"
          onClose={() => setError("")}
        >
          {error}
        </Alert>
      )}

      {/* =====================================================
          MAIN GRID
      ====================================================== */}

      <Box className="gesture-grid">
        {/* ===================================================
            CAMERA
        ==================================================== */}

        <Card className="gesture-card camera-card">
          <CardContent>
            <Box className="card-heading">
              <Box>
                <Typography className="card-label">LIVE CAMERA</Typography>

                <Typography variant="h6" className="card-title">
                  Show your gesture
                </Typography>
              </Box>

              {recording && (
                <Box className="recording-indicator">
                  <span />
                  RECORDING
                </Box>
              )}
            </Box>

            <Box className="camera-container">
              {cameraActive ? (
                <video
                  ref={videoRef}
                  autoPlay
                  muted
                  playsInline
                  className="camera-video"
                />
              ) : (
                <Box className="camera-placeholder">
                  <CameraAlt />

                  <Typography>Camera preview will appear here</Typography>

                  <Typography variant="body2">
                    Position both hands clearly inside the frame.
                  </Typography>
                </Box>
              )}

              {recording && (
                <Box className="recording-overlay">
                  <Box className="recording-timer">{remainingTime}s</Box>
                </Box>
              )}
            </Box>

            <Stack direction="row" spacing={1.5} className="camera-actions">
              {!cameraActive ? (
                <Button
                  variant="contained"
                  startIcon={<CameraAlt />}
                  onClick={startCamera}
                  className="primary-button"
                >
                  Start Camera
                </Button>
              ) : (
                <Button
                  variant="outlined"
                  onClick={stopCamera}
                  disabled={recording || processing}
                  className="secondary-button"
                >
                  Stop Camera
                </Button>
              )}

              {cameraActive && !recording && (
                <Button
                  variant="contained"
                  startIcon={<CameraAlt />}
                  onClick={startRecording}
                  disabled={processing}
                  className="primary-button"
                >
                  Recognize Gesture
                </Button>
              )}

              {recording && (
                <Button
                  variant="outlined"
                  color="error"
                  startIcon={<Stop />}
                  onClick={stopRecording}
                  className="stop-button"
                >
                  Stop Recording
                </Button>
              )}
            </Stack>
          </CardContent>
        </Card>

        {/* ===================================================
            RESULT
        ==================================================== */}

        <Card className="gesture-card result-card">
          <CardContent>
            <Typography className="card-label">AI RECOGNITION</Typography>

            <Typography variant="h6" className="card-title">
              Detection Result
            </Typography>

            {processing ? (
              <Box className="processing-state">
                <CircularProgress size={42} thickness={4} />

                <Typography className="processing-title">
                  Analyzing gesture...
                </Typography>

                <Typography variant="body2" className="processing-text">
                  MediaPipe is extracting hand landmarks and Model 3 is
                  recognizing your gesture.
                </Typography>
              </Box>
            ) : result ? (
              <Box className="result-content">
                <Box className="gesture-result-box">
                  <Typography className="result-label">
                    DETECTED GESTURE
                  </Typography>

                  <Typography className="detected-gesture">
                    {result.gesture?.replace(/_/g, " ")}
                  </Typography>
                </Box>

                <Box className="confidence-section">
                  <Box className="confidence-header">
                    <Typography>Confidence</Typography>

                    <Typography>{result.confidence}%</Typography>
                  </Box>

                  <LinearProgress
                    variant="determinate"
                    value={result.confidence || 0}
                    className="confidence-bar"
                  />
                </Box>

                {displayMessage && (
                  <>
                    <Divider />

                    <Box className="message-section">
                      <Typography className="result-label">
                        COMMUNICATION MESSAGE
                      </Typography>

                      <Typography className="gesture-message">
                        {displayMessage}
                      </Typography>

                      <Button
                        variant="outlined"
                        startIcon={<VolumeUp />}
                        onClick={speakGesture}
                        className="speak-button"
                      >
                        Speak Message
                      </Button>
                    </Box>
                  </>
                )}

                {!result.recognized && (
                  <Alert severity="warning" className="low-confidence-alert">
                    Gesture confidence is too low. Please try again with your
                    hands clearly visible.
                  </Alert>
                )}

                <Typography variant="caption" className="processing-time">
                  Processing time: {result.processing_time_ms} ms
                </Typography>
              </Box>
            ) : (
              <Box className="empty-result">
                <Box className="empty-icon">
                  <Replay />
                </Box>

                <Typography className="empty-title">
                  No gesture detected yet
                </Typography>

                <Typography variant="body2" className="empty-text">
                  Start the camera and click "Recognize Gesture" to begin.
                </Typography>
              </Box>
            )}
          </CardContent>
        </Card>
      </Box>

      {/* =====================================================
          SUPPORTED GESTURES
      ====================================================== */}

      <Card className="supported-card">
        <CardContent>
          <Typography className="card-label">SUPPORTED GESTURES</Typography>

          <Typography variant="h6" className="card-title">
            Emergency communication
          </Typography>

          <Box className="gesture-list">
            {Object.keys(gestureMessages).map((gesture) => (
              <Box key={gesture} className="supported-gesture">
                <Typography>{gesture.replace(/_/g, " ")}</Typography>

                <Typography variant="body2">
                  {gestureMessages[gesture]}
                </Typography>
              </Box>
            ))}
          </Box>
        </CardContent>
      </Card>
    </Box>
  );
}

export default GestureDetection;
