import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
  headers: {
    "Content-Type": "multipart/form-data",
  },
});

export const checkBackendHealth = async () => {
  return await api.get("/health");
};

export const processAudio = async (audioBlob) => {
  const formData = new FormData();

  formData.append("file", audioBlob, "recording.wav");

  const response = await api.post("/process-audio", formData);

  return response.data;
};

export default api;
