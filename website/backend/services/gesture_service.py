import cv2
import mediapipe as mp
import numpy as np
import tempfile
import os
import time

from core.model_manager import ModelManager
from core.config import (
    GESTURE_ACTIONS,
    GESTURE_SEQUENCE_LENGTH,
    GESTURE_CONFIDENCE_THRESHOLD,
)


# ============================================================
# MediaPipe Hands
# ============================================================

mp_hands = mp.solutions.hands


# ============================================================
# Extract Keypoints
# ============================================================

def extract_landmarks(results):
    """
    EXACTLY matches the preprocessing used during
    Model 3 inference.

    Left hand  = 63 values
    Right hand = 63 values

    Total = 126 features
    """

    left_hand = np.zeros(
        21 * 3,
        dtype=np.float32
    )

    right_hand = np.zeros(
        21 * 3,
        dtype=np.float32
    )

    if (
        results.multi_hand_landmarks
        and results.multi_handedness
    ):

        for idx, hand_handedness in enumerate(
            results.multi_handedness
        ):

            hand_label = (
                hand_handedness
                .classification[0]
                .label
            )

            hand_landmarks = (
                results.multi_hand_landmarks[idx]
            )

            coordinates = np.array(
                [
                    [
                        landmark.x,
                        landmark.y,
                        landmark.z,
                    ]
                    for landmark
                    in hand_landmarks.landmark
                ],
                dtype=np.float32,
            ).flatten()

            if hand_label == "Left":

                left_hand = coordinates

            elif hand_label == "Right":

                right_hand = coordinates

    return np.concatenate(
        [
            left_hand,
            right_hand,
        ]
    )


# ============================================================
# Extract Video Sequence
# ============================================================

def extract_gesture_sequence(video_path):

    cap = cv2.VideoCapture(
        video_path
    )

    if not cap.isOpened():
        raise ValueError(
            "Unable to open uploaded video."
        )

    sequence = []

    try:

        with mp_hands.Hands(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
            max_num_hands=2,
        ) as hands_detector:

            while (
                cap.isOpened()
                and len(sequence)
                < GESTURE_SEQUENCE_LENGTH
            ):

                ret, frame = cap.read()

                if not ret:
                    break

                # --------------------------------------------
                # BGR → RGB
                # --------------------------------------------

                image_rgb = cv2.cvtColor(
                    frame,
                    cv2.COLOR_BGR2RGB
                )

                # --------------------------------------------
                # MediaPipe
                # --------------------------------------------

                results = hands_detector.process(
                    image_rgb
                )

                # --------------------------------------------
                # Extract 126 features
                # --------------------------------------------

                keypoints = extract_landmarks(
                    results
                )

                sequence.append(
                    keypoints
                )

    finally:

        cap.release()

        time.sleep(0.1)

    # ========================================================
    # Handle empty video
    # ========================================================

    if len(sequence) == 0:

        sequence = [
            np.zeros(
                126,
                dtype=np.float32
            )
        ]

    # ========================================================
    # Pad to exactly 90 frames
    # ========================================================

    while len(sequence) < GESTURE_SEQUENCE_LENGTH:

        sequence.append(
            sequence[-1].copy()
        )

    # ========================================================
    # Ensure exactly 90 frames
    # ========================================================

    sequence = sequence[
        :GESTURE_SEQUENCE_LENGTH
    ]

    sequence_data = np.array(
        sequence,
        dtype=np.float32
    )

    # ========================================================
    # Validate
    # ========================================================

    expected_shape = (
        GESTURE_SEQUENCE_LENGTH,
        126,
    )

    if sequence_data.shape != expected_shape:

        raise ValueError(
            f"Invalid gesture sequence shape: "
            f"{sequence_data.shape}. "
            f"Expected {expected_shape}."
        )

    return sequence_data


# ============================================================
# Predict Gesture
# ============================================================

def predict_gesture(video_path):

    if ModelManager.gesture_model is None:

        raise RuntimeError(
            "Gesture recognition model "
            "is not loaded."
        )

    # --------------------------------------------------------
    # Extract sequence
    # --------------------------------------------------------

    sequence_data = extract_gesture_sequence(
        video_path
    )

    # --------------------------------------------------------
    # Add batch dimension
    # --------------------------------------------------------

    model_input = np.expand_dims(
        sequence_data,
        axis=0
    )

    # --------------------------------------------------------
    # Predict
    # --------------------------------------------------------

    predictions = (
        ModelManager.gesture_model.predict(
            model_input,
            verbose=0
        )
    )

    probabilities = predictions[0]

    predicted_index = int(
        np.argmax(probabilities)
    )

    confidence = float(
        probabilities[predicted_index]
    )

    gesture = GESTURE_ACTIONS[
        predicted_index
    ]

    # --------------------------------------------------------
    # Confidence threshold
    # --------------------------------------------------------

    if (
        confidence
        < GESTURE_CONFIDENCE_THRESHOLD
    ):

        return {
            "gesture": "UNKNOWN",
            "confidence": round(
                confidence * 100,
                2
            ),
            "recognized": False,
        }

    return {
        "gesture": gesture,
        "confidence": round(
            confidence * 100,
            2
        ),
        "recognized": True,
    }


# ============================================================
# Process Uploaded Video
# ============================================================

def process_gesture_video(
    video_bytes,
    filename="gesture.webm"
):

    temp_path = None

    try:

        # ----------------------------------------------------
        # Preserve uploaded extension
        # ----------------------------------------------------

        extension = os.path.splitext(
            filename
        )[1].lower()

        supported_extensions = {
            ".mp4",
            ".webm",
            ".mov",
            ".avi",
            ".mkv",
        }

        if extension not in supported_extensions:
            extension = ".webm"

        # ----------------------------------------------------
        # Create temporary file
        # ----------------------------------------------------

        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=extension
        )

        temp_path = temp_file.name

        try:

            temp_file.write(
                video_bytes
            )

            temp_file.flush()

        finally:

            # Important on Windows:
            # close before OpenCV opens the file.
            temp_file.close()

        # ----------------------------------------------------
        # Run Model 3
        # ----------------------------------------------------

        result = predict_gesture(
            temp_path
        )

        return result

    finally:

        # ----------------------------------------------------
        # Cleanup
        # ----------------------------------------------------

        if (
            temp_path
            and os.path.exists(temp_path)
        ):

            try:

                os.remove(temp_path)

            except PermissionError:

                print(
                    "Warning: Could not immediately "
                    "delete temporary gesture video:"
                )

                print(temp_path)