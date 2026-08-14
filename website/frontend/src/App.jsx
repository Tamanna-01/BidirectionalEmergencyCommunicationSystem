import { Navigate, Route, Routes } from "react-router-dom";

import MainLayout from "./layouts/MainLayout";

import Dashboard from "./pages/Dashboard/Dashboard";
import AudioDetection from "./pages/AudioDetection/AudioDetection";
import GestureDetection from "./pages/GestureDetection/GestureDetection";

function App() {
  return (
    <Routes>
      <Route element={<MainLayout />}>
        <Route path="/" element={<Navigate to="/dashboard" replace />} />

        <Route path="/dashboard" element={<Dashboard />} />

        <Route path="/audio-detection" element={<AudioDetection />} />

        <Route path="/gesture-detection" element={<GestureDetection />} />
      </Route>
    </Routes>
  );
}

export default App;
