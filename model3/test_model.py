import cv2
import numpy as np
import mediapipe as mp
import pyttsx3
import threading
import os

# Force TensorFlow to use the stable Keras 2 engine
os.environ['TF_USE_LEGACY_KERAS'] = '1'
from tf_keras.models import load_model

# --- 1. Configuration ---
actions = np.array(['HELP', 'CALL_AMBULANCE', 'FIRE', 'CALL_DOCTOR', 'STOP_DANGER'])
sequence_length = 90
threshold = 0.80  # The model must be 80% confident to trigger the speech

# --- 2. Initialize Text-to-Speech ---
engine = pyttsx3.init()
engine.setProperty('rate', 150) # Speed of speech

def speak(text):
    """Speaks the text in a separate thread to prevent the video feed from freezing."""
    engine.say(text)
    engine.runAndWait()

# --- 3. Load Model ---
print("Loading model...")
model = load_model('action.h5')
print("Model loaded successfully!")

# --- 4. MediaPipe Setup ---
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

def extract_keypoints(results):
    lh = np.zeros(21 * 3)
    rh = np.zeros(21 * 3)
    if results.multi_hand_landmarks and results.multi_handedness:
        for idx, hand_handedness in enumerate(results.multi_handedness):
            hand_label = hand_handedness.classification[0].label
            hand_landmarks = results.multi_hand_landmarks[idx]
            coords = np.array([[lm.x, lm.y, lm.z] for lm in hand_landmarks.landmark]).flatten()
            if hand_label == 'Left':
                lh = coords
            elif hand_label == 'Right':
                rh = coords
    return np.concatenate([lh, rh])

# --- 5. Real-Time Prediction Loop ---
sequence = []
current_action = ""

cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=2) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: 
            break
        frame = cv2.flip(frame, 1)
        
        # Process frame
        image, results = frame, hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        
        # Draw landmarks
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        
        # Extract keypoints and build sequence
        keypoints = extract_keypoints(results)
        sequence.append(keypoints)
        
        # Keep only the last 90 frames
        sequence = sequence[-sequence_length:]
        
        # Predict if we have exactly 90 frames
        if len(sequence) == sequence_length:
            # Model expects shape (1, 90, 126)
            res = model.predict(np.expand_dims(sequence, axis=0), verbose=0)[0]
            
            # If the highest probability is greater than our 80% threshold
            if res[np.argmax(res)] > threshold:
                predicted_action = actions[np.argmax(res)]
                
                # Only trigger speech if it's a NEW action
                if predicted_action != current_action:
                    current_action = predicted_action
                    
                    # Format the text
                    spoken_text = current_action.replace('_', ' ')
                    threading.Thread(target=speak, args=(spoken_text,)).start()
        
        # UI Display
        cv2.putText(image, f'Prediction: {current_action.replace("_", " ")}', (15, 40), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        
        cv2.imshow('Live ISL Translation', image)
        
        # Press 'q' to quit
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()