import cv2
import numpy as np
import os
import mediapipe as mp

# --- Configuration ---
ACTION_NAME = 'STOP_DANGER'  

DATA_PATH = os.path.join(os.path.abspath('.'), 'Emergency_ISL_Dataset')
no_sequences = 50        
sequence_length = 90     

os.makedirs(os.path.join(DATA_PATH, ACTION_NAME), exist_ok=True)
print(f"Dataset for {ACTION_NAME} will be saved locally at: {os.path.join(DATA_PATH, ACTION_NAME)}")

# --- MediaPipe Setup ---
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

def extract_keypoints(results):
    """Extracts and flattens left and right hand landmarks into a (126,) array."""
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

# --- Capture Loop ---
cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=2) as hands:
    for sequence in range(no_sequences):
        sequence_data = [] 
        
        for frame_num in range(sequence_length):
            ret, frame = cap.read()
            frame = cv2.flip(frame, 1) 
            
            # Convert BGR to RGB for MediaPipe
            image, results = frame, hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            
            # Draw landmarks on screen
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Collection logic & UI
            if frame_num == 0: 
                cv2.putText(image, 'GET READY...', (120, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 4, cv2.LINE_AA)
                cv2.putText(image, f'Action: {ACTION_NAME} | Video: {sequence}/50', (15, 30), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2, cv2.LINE_AA)
                cv2.imshow('OpenCV Feed', image)
                cv2.waitKey(2000) 
            else: 
                cv2.putText(image, f'Action: {ACTION_NAME} | Video: {sequence}/50 | Frame: {frame_num}/90', (15, 30), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2, cv2.LINE_AA)
                cv2.imshow('OpenCV Feed', image)
            
            # Extract and store keypoints for this frame
            keypoints = extract_keypoints(results)
            sequence_data.append(keypoints)
            
            # Break gracefully if 'q' is pressed
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        
        # Save the 90-frame sequence as a numpy array
        npy_path = os.path.join(DATA_PATH, ACTION_NAME, f'{sequence}.npy')
        np.save(npy_path, np.array(sequence_data))
        
cap.release()
cv2.destroyAllWindows()