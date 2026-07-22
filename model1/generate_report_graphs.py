import os
import numpy as np
import librosa
import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# 1. Define Paths
base_dir = r"C:\Users\Tamanna Shaw\Downloads\IIIT-Dharwad\Project\ProjectCode\BidirectionalEmergencyCommunicationSystem\model1"
dataset_dir = os.path.join(base_dir, "dataset_final")
model_path = os.path.join(base_dir, "emergency_sound_model.h5")
classes_path = os.path.join(base_dir, "class_names.npy")

# 2. Load Model & Yamnet
print("Loading saved model and YAMNet...")
custom_model = tf.keras.models.load_model(model_path)
class_names = np.load(classes_path)
yamnet_model = hub.load('https://tfhub.dev/google/yamnet/1')

def extract_embedding(file_path):
    wav_data, _ = librosa.load(file_path, sr=16000, mono=True)
    wav_data, _ = librosa.effects.trim(wav_data, top_db=20)
    wav_data = wav_data / tf.math.reduce_max(tf.math.abs(wav_data) + 1e-8)
    waveform = tf.convert_to_tensor(wav_data, dtype=tf.float32)
    _, embeddings, _ = yamnet_model(waveform)
    return tf.reduce_mean(embeddings, axis=0).numpy()

# 3. Process Data (We must recreate the exact same Validation set using random_state=42)
print("Extracting embeddings to generate graphs (this takes a few minutes)...")
X, y = [], []
classes_in_dir = [f for f in os.listdir(dataset_dir) if os.path.isdir(os.path.join(dataset_dir, f))]

for cls in classes_in_dir:
    class_dir = os.path.join(dataset_dir, cls)
    for file_name in os.listdir(class_dir):
        if file_name.endswith('.wav'):
            try:
                X.append(extract_embedding(os.path.join(class_dir, file_name)))
                y.append(cls)
            except:
                pass

X = np.array(X)
y = np.array(y)

# Use the exact same seed as training to isolate the unseen test data
_, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Generate Predictions
print("Generating predictions on unseen test data...")
y_pred_probs = custom_model.predict(X_test)
y_pred_indices = np.argmax(y_pred_probs, axis=1)
y_pred_labels = [class_names[i] for i in y_pred_indices]

# 5. Graph 1: Confusion Matrix
cm = confusion_matrix(y_test, y_pred_labels, labels=class_names)
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
plt.title('Confusion Matrix: Emergency Sound Classification')
plt.ylabel('Actual Sound')
plt.xlabel('Predicted Sound')
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 'confusion_matrix.png'))
plt.show()

# 6. Generate Classification Report
print("\n================ CLASSIFICATION REPORT ================")
report = classification_report(y_test, y_pred_labels, target_names=class_names)
print(report)