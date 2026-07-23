# import os
# import numpy as np
# import librosa
# import tensorflow as tf
# import tensorflow_hub as hub
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
# from sklearn.utils.class_weight import compute_class_weight
# from tensorflow.keras import layers, models, regularizers
# from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau

# # 1. Define hardcoded paths
# base_dir = r"C:\Users\Tamanna Shaw\Downloads\IIIT-Dharwad\Project\ProjectCode\BidirectionalEmergencyCommunicationSystem\model1"
# dataset_dir = os.path.join(base_dir, "dataset_final")
# model_save_path = os.path.join(base_dir, "emergency_sound_model.h5")
# classes_save_path = os.path.join(base_dir, "class_names.npy")

# # 2. Load the Pre-Trained YAMNet Model
# print("Loading pre-trained YAMNet model from TF Hub...")
# yamnet_model_handle = 'https://tfhub.dev/google/yamnet/1'
# yamnet_model = hub.load(yamnet_model_handle)

# # 3. Function to Extract 1024-d Embeddings
# def extract_embedding(file_path):
#     wav_data, _ = librosa.load(file_path, sr=16000, mono=True)
#     wav_data = wav_data / tf.math.reduce_max(tf.math.abs(wav_data) + 1e-8)
#     waveform = tf.convert_to_tensor(wav_data, dtype=tf.float32)
#     scores, embeddings, spectrogram = yamnet_model(waveform)
#     return tf.reduce_mean(embeddings, axis=0).numpy()

# # 4. Process the Dataset
# print("\nExtracting embeddings from audio files...")
# X = []
# y = []

# class_names = [f for f in os.listdir(dataset_dir) if os.path.isdir(os.path.join(dataset_dir, f))]

# for class_name in class_names:
#     class_dir = os.path.join(dataset_dir, class_name)
#     print(f"Processing class: {class_name}")
#     for file_name in os.listdir(class_dir):
#         if file_name.endswith('.wav'):
#             file_path = os.path.join(class_dir, file_name)
#             try:
#                 X.append(extract_embedding(file_path))
#                 y.append(class_name)
#             except Exception as e:
#                 pass

# X = np.array(X)
# y = np.array(y)

# # 5. Encode Labels & Split Data
# print("\nPreparing data for training...")
# encoder = LabelEncoder()
# y_encoded = encoder.fit_transform(y)
# num_classes = len(encoder.classes_)

# X_train, X_val, y_train, y_val = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# # Compute Class Weights to fix the imbalance
# class_weights = compute_class_weight(
#     class_weight='balanced',
#     classes=np.unique(y_train),
#     y=y_train
# )
# class_weights_dict = dict(enumerate(class_weights))
# print("\nComputed Class Weights:", class_weights_dict)

# # 6. Build the Classification Model
# print("Building the optimized classification model...")
# model = models.Sequential([
#     layers.Input(shape=(1024,), name='input_embedding'),
    
#     # Relaxed L2 Regularization (0.001 instead of 0.005)
#     layers.Dense(512, activation='relu', kernel_regularizer=regularizers.l2(0.001)),
#     layers.BatchNormalization(),
#     layers.Dropout(0.5),
    
#     layers.Dense(256, activation='relu', kernel_regularizer=regularizers.l2(0.001)),
#     layers.BatchNormalization(),
#     layers.Dropout(0.5),
    
#     layers.Dense(num_classes, activation='softmax')
# ])

# model.compile(
#     optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), 
#     loss='sparse_categorical_crossentropy', 
#     metrics=['accuracy']
# )

# # 7. Define Callbacks
# early_stopping = EarlyStopping(monitor='val_accuracy', patience=15, restore_best_weights=True, verbose=1)
# reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=5, min_lr=1e-6, verbose=1)
# model_checkpoint = ModelCheckpoint(filepath=model_save_path, monitor='val_accuracy', save_best_only=True, mode='max', verbose=1)

# # 8. Train the Model with Class Weights
# print("\nStarting training with class weights...")
# history = model.fit(
#     X_train, y_train, 
#     epochs=100, 
#     batch_size=32, 
#     validation_data=(X_val, y_val),
#     class_weight=class_weights_dict, # Applying the mathematical weights here!
#     callbacks=[early_stopping, reduce_lr, model_checkpoint]
# )

# np.save(classes_save_path, encoder.classes_)
# print("\n================ TRAINING COMPLETE ================")


import os
import numpy as np
import librosa
import tensorflow as tf
import tensorflow_hub as hub
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.utils.class_weight import compute_class_weight
from tensorflow.keras import layers, models, regularizers
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau

# 1. Define hardcoded paths
base_dir = r"C:\Users\Tamanna Shaw\Downloads\IIIT-Dharwad\Project\ProjectCode\BidirectionalEmergencyCommunicationSystem\model1"
dataset_dir = os.path.join(base_dir, "dataset_final")
model_save_path = os.path.join(base_dir, "emergency_sound_model.h5")
classes_save_path = os.path.join(base_dir, "class_names.npy")

print("Loading pre-trained YAMNet model from TF Hub...")
yamnet_model_handle = 'https://tfhub.dev/google/yamnet/1'
yamnet_model = hub.load(yamnet_model_handle)

# 3. Trim Dead Air & Extract Embeddings
def extract_embedding(file_path):
    wav_data, _ = librosa.load(file_path, sr=16000, mono=True)
    
    # NEW: Automatically trim silence from the beginning and end of the clip (Threshold: 20 decibels)
    wav_data, _ = librosa.effects.trim(wav_data, top_db=20)
    
    wav_data = wav_data / tf.math.reduce_max(tf.math.abs(wav_data) + 1e-8)
    waveform = tf.convert_to_tensor(wav_data, dtype=tf.float32)
    scores, embeddings, spectrogram = yamnet_model(waveform)
    return tf.reduce_mean(embeddings, axis=0).numpy()

print("\nExtracting embeddings from audio files...")
X = []
y = []

class_names = [f for f in os.listdir(dataset_dir) if os.path.isdir(os.path.join(dataset_dir, f))]

for class_name in class_names:
    class_dir = os.path.join(dataset_dir, class_name)
    print(f"Processing class: {class_name}")
    for file_name in os.listdir(class_dir):
        if file_name.endswith('.wav'):
            file_path = os.path.join(class_dir, file_name)
            try:
                X.append(extract_embedding(file_path))
                y.append(class_name)
            except Exception as e:
                pass

X = np.array(X)
y = np.array(y)

print("\nPreparing data for training...")
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)
num_classes = len(encoder.classes_)

X_train, X_val, y_train, y_val = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

class_weights = compute_class_weight(
    class_weight='balanced',
    classes=np.unique(y_train),
    y=y_train
)
class_weights_dict = dict(enumerate(class_weights))
print("\nComputed Class Weights:", class_weights_dict)

print("Building the optimized classification model...")
model = models.Sequential([
    layers.Input(shape=(1024,), name='input_embedding'),
    layers.Dense(512, activation='relu', kernel_regularizer=regularizers.l2(0.001)),
    layers.BatchNormalization(),
    layers.Dropout(0.5),
    layers.Dense(256, activation='relu', kernel_regularizer=regularizers.l2(0.001)),
    layers.BatchNormalization(),
    layers.Dropout(0.5),
    layers.Dense(num_classes, activation='softmax')
])

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), 
    loss='sparse_categorical_crossentropy', 
    metrics=['accuracy']
)

early_stopping = EarlyStopping(monitor='val_accuracy', patience=15, restore_best_weights=True, verbose=1)
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=5, min_lr=1e-6, verbose=1)
model_checkpoint = ModelCheckpoint(filepath=model_save_path, monitor='val_accuracy', save_best_only=True, mode='max', verbose=1)

print("\nStarting training on fully balanced, trimmed dataset...")
history = model.fit(
    X_train, y_train, 
    epochs=100, 
    batch_size=32, 
    validation_data=(X_val, y_val),
    class_weight=class_weights_dict, 
    callbacks=[early_stopping, reduce_lr, model_checkpoint]
)

np.save(classes_save_path, encoder.classes_)
print("\n================ TRAINING COMPLETE ================")