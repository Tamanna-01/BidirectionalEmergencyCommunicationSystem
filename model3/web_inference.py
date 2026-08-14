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
threshold = 0.80

# --- 2. Initialize Globals for Web Backend ---
# We load the model and MediaPipe once here so your web server doesn't 
# have to reload them from scratch every time a user uploads a video.
print("Booting up translation engine...")
model = load_model('action.h5')
mp_hands = mp.solutions.hands
hands_detector = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=2)

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    """Speaks text in a separate thread so it doesn't block the web server."""
    engine.say(text)
    engine.runAndWait()

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

# --- 3. The Core Web Function ---
def translate_video(video_filepath):
    """
    Takes a path to a 3-second video file (e.g., recorded from a web browser),
    processes the frames, and returns a JSON-friendly dictionary.
    """
    cap = cv2.VideoCapture(video_filepath)
    sequence = []
    
    # Process up to 90 frames from the uploaded video
    while cap.isOpened() and len(sequence) < sequence_length:
        ret, frame = cap.read()
        if not ret:
            break
            
        # MediaPipe processing
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands_detector.process(image_rgb)
        
        keypoints = extract_keypoints(results)
        sequence.append(keypoints)

    cap.release()

    # Video length normalization: 
    # If the web video was slightly shorter than 90 frames, pad the end with the last known position.
    while len(sequence) < sequence_length:
        if len(sequence) > 0:
            sequence.append(sequence[-1])
        else:
            sequence.append(np.zeros(126)) # Fallback if video is completely empty

    # Convert to numpy array and predict
    sequence_data = np.array(sequence)
    res = model.predict(np.expand_dims(sequence_data, axis=0), verbose=0)[0]
    
    max_idx = np.argmax(res)
    confidence = res[max_idx]

    # Check confidence threshold
    if confidence > threshold:
        predicted_action = actions[max_idx]
        spoken_text = predicted_action.replace('_', ' ')
        
        # Trigger the speech module
        threading.Thread(target=speak, args=(spoken_text,)).start()
        
        # Return a dictionary that your web framework (Flask/FastAPI/Django) can easily send to the frontend
        return {
            "success": True,
            "prediction": predicted_action,
            "display_text": spoken_text,
            "confidence": float(confidence)
        }
    else:
        return {
            "success": False,
            "prediction": "Unknown",
            "display_text": "Sign not recognized. Please try again.",
            "confidence": float(confidence)
        }

# --- 4. Local Testing ---
if __name__ == "__main__":
    print("Backend script ready. Import 'translate_video' into your web app routing file.")
    
    # To test this locally before hooking it up to your website, you can uncomment the lines below 
    # and provide a path to a test video:
    # 
    test_result = translate_video("call_doc.mp4")
    print(test_result)