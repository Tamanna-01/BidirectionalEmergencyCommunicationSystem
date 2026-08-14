import numpy as np
import os

# Force TensorFlow to use the stable Keras 2 engine
os.environ['TF_USE_LEGACY_KERAS'] = '1'

from sklearn.model_selection import train_test_split
from tf_keras.utils import to_categorical
from tf_keras.models import Sequential
from tf_keras.layers import LSTM, Dense, Dropout

# --- 1. Configuration ---
DATA_PATH = os.path.join(os.path.abspath('.'), 'Emergency_ISL_Dataset')
actions = np.array(['HELP', 'CALL_AMBULANCE', 'FIRE', 'CALL_DOCTOR', 'STOP_DANGER'])
no_sequences = 50
sequence_length = 90

# --- 2. Data Preprocessing ---
print("Loading data from dataset...")
label_map = {label:num for num, label in enumerate(actions)}

sequences, labels = [], []
for action in actions:
    for sequence in range(no_sequences):
        res = np.load(os.path.join(DATA_PATH, action, f"{sequence}.npy"))
        sequences.append(res)
        labels.append(label_map[action])

X = np.array(sequences)
y = to_categorical(labels).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)
print(f"Data loaded! Training shape: {X_train.shape}")

# --- 3. Build the LSTM Architecture ---
print("Building Stable LSTM Model...")
model = Sequential()

model.add(LSTM(64, return_sequences=True, input_shape=(90, 126)))
model.add(Dropout(0.2))
model.add(LSTM(128, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(64, return_sequences=False))
model.add(Dropout(0.2))

model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(actions.shape[0], activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])

# --- 4. Train the Model ---
print("Starting training...")
model.fit(X_train, y_train, epochs=150)

# --- 5. Save the Model ---
model.save('action.h5')
print("Model successfully trained and saved as 'action.h5'!")