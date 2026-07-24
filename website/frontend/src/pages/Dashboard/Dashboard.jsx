import React from "react";
import { useNavigate } from "react-router-dom";
import "./Dashboard.css";

const Dashboard = () => {
  const navigate = useNavigate();

  return (
    <div className="dashboard-page">
      {/* Hero Section */}
      <section className="hero-section">
        <div className="hero-content">
          <h1 className="hero-title">AI Emergency Communication System</h1>
          <p className="hero-subtitle">Real-time Bidirectional Support</p>
          <p className="hero-description">
            An accessible, life-saving bridge for the deaf and hard-of-hearing
            community during critical crises. Our platform proactively analyzes
            ambient noise and human voices while supporting two-way
            communication through Indian Sign Language (ISL) translation.
          </p>
        </div>
      </section>

      {/* Problem & Solution Section */}
      <section className="content-section">
        <h2 className="section-title">System Overview</h2>
        <p className="section-subtitle">
          Understanding the communication gap and our multimodal solution.
        </p>

        <div className="cards-grid-2">
          {/* The Problem */}
          <div className="info-card workflow-card light-bg">
            <h3 className="feature-title">The Problem</h3>
            <ul className="feature-description list-spaced">
              <li>
                Traditional emergency frameworks rarely address the unique needs
                of individuals with hearing disabilities.
              </li>
              <li>
                During disasters, communication heavily relies on auditory cues
                (sirens, verbal instructions), cutting off the deaf community.
              </li>
              <li>
                Globally, people with disabilities face fatality rates two to
                four times higher than the general population.
              </li>
              <li>
                In India, this issue is exacerbated by a severe shortage of
                trained Indian Sign Language (ISL) interpreters.
              </li>
              <li>
                Current technology systems struggle to process convoluted,
                non-essential speech in chaotic acoustic environments.
              </li>
            </ul>
          </div>

          {/* The Solution */}
          <div className="info-card workflow-card light-bg">
            <h3 className="feature-title">The Solution</h3>
            <ul className="feature-description list-spaced">
              <li>
                An AI-Powered Bidirectional Emergency Communication System
                acting as a life-saving bridge.
              </li>
              <li>
                A real-time, multimodal platform that uses generative AI to
                analyze ambient noise and human voices.
              </li>
              <li>
                Proactively translates a user's sign language into text and
                speech for others to understand.
              </li>
              <li>
                Summarizes chaotic environmental audio and complex verbal
                instructions into ultra-concise, actionable text phrases for the
                user.
              </li>
            </ul>
          </div>
        </div>
      </section>

      {/* Key Features Section */}
      <section className="content-section">
        <h2 className="section-title">Key Features</h2>
        <p className="section-subtitle">
          Core capabilities powering the bidirectional communication system.
        </p>

        <div className="cards-grid-3">
          <div className="info-card workflow-card white-bg">
            <div className="feature-icon">🎙️</div>
            <h3 className="feature-title">Continuous Monitoring</h3>
            <p className="feature-description">
              Actively monitors surrounding environmental sounds in real-time
              using the device microphone.
            </p>
          </div>

          <div className="info-card workflow-card white-bg">
            <div className="feature-icon">🚨</div>
            <h3 className="feature-title">Sound Detection</h3>
            <p className="feature-description">
              Fine-tuned YAMNet model detects emergency-specific sounds like
              sirens, gunshots, explosions, and cries for help.
            </p>
          </div>

          <div className="info-card workflow-card white-bg">
            <div className="feature-icon">📝</div>
            <h3 className="feature-title">Speech-to-Text</h3>
            <p className="feature-description">
              Captures human speech, converts it to text, and uses rule-based
              keyword detection to confirm emergencies.
            </p>
          </div>

          <div className="info-card workflow-card white-bg">
            <div className="feature-icon">⚡</div>
            <h3 className="feature-title">AI Simplification</h3>
            <p className="feature-description">
              A fine-tuned FLAN-T5 Generative AI model simplifies complex verbal
              instructions into short, clear, actionable phrases.
            </p>
          </div>

          <div className="info-card workflow-card white-bg">
            <div className="feature-icon">📳</div>
            <h3 className="feature-title">Actionable Alerts</h3>
            <p className="feature-description">
              Delivers simplified instructions instantly through visual
              notifications and device vibrations, bypassing the need for
              hearing.
            </p>
          </div>

          <div className="info-card workflow-card white-bg">
            <div className="feature-icon">🤟</div>
            <h3 className="feature-title">ISL Recognition</h3>
            <p className="feature-description">
              Captures hand gestures via camera and processes them using
              MediaPipe and an LSTM-based classification model.
            </p>
          </div>
        </div>
      </section>

      {/* CTA Section with Navigation Buttons */}
      <section className="cta-section">
        <h2 className="cta-title">Ready to Initialize?</h2>
        <p className="cta-description">
          Activate the dashboard to begin real-time audio monitoring or launch
          the camera module for bidirectional ISL translation.
        </p>

        <div className="hero-buttons cta-buttons">
          <button
            className="primary-btn"
            onClick={() => navigate("/audio-detection")}
          >
            Launch Audio Detection
          </button>

          <button
            className="primary-btn"
            onClick={() => navigate("/gesture-detection")}
          >
            Launch Gesture Detection
          </button>
        </div>
      </section>
    </div>
  );
};

export default Dashboard;
