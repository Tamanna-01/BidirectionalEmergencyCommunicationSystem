import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

// ============================================================
// Backend Health
// ============================================================

export const checkBackendHealth = async () => {
  return await api.get("/health");
};

// ============================================================
// Audio Detection - Model 1 + Model 2
// ============================================================

export const processAudio = async (audioBlob) => {
  const formData = new FormData();

  formData.append("file", audioBlob, "recording.wav");

  const response = await api.post("/process-audio", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return response.data;
};

// ============================================================
// Gesture Recognition - Model 3
// ============================================================

export const processGesture = async (videoBlob) => {
  const formData = new FormData();

  formData.append("file", videoBlob, "gesture.webm");

  const response = await api.post("/gesture-detection", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return response.data;
};

export default api;
