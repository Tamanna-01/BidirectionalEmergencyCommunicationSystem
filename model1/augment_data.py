# import os
# import random
# import librosa
# import numpy as np
# import soundfile as sf

# # 1. Hardcoded paths
# base_dir = r"C:\Users\Tamanna Shaw\Downloads\IIIT-Dharwad\Project\ProjectCode\BidirectionalEmergencyCommunicationSystem\model1"
# dataset_dir = os.path.join(base_dir, "dataset_final")

# # Set the target number of files for every class
# TARGET_COUNT = 200

# # 2. Define Augmentation Techniques
# def add_noise(data, noise_factor=0.005):
#     """Injects light static/background noise."""
#     noise = np.random.randn(len(data))
#     return data + noise_factor * noise

# def time_stretch(data, rate):
#     """Speeds up or slows down the audio without changing pitch."""
#     return librosa.effects.time_stretch(y=data, rate=rate)

# def pitch_shift(data, sr, n_steps):
#     """Raises or lowers the pitch (e.g., a higher or lower siren)."""
#     return librosa.effects.pitch_shift(y=data, sr=sr, n_steps=n_steps)

# print("Starting Data Augmentation...")

# # 3. Process Each Class Folder
# class_names = [f for f in os.listdir(dataset_dir) if os.path.isdir(os.path.join(dataset_dir, f))]

# for class_name in class_names:
#     class_dir = os.path.join(dataset_dir, class_name)
    
#     # Only grab original files (ignore ones we've already augmented if script is run twice)
#     original_files = [f for f in os.listdir(class_dir) if f.endswith('.wav') and not f.startswith('aug_')]
#     current_count = len(original_files)
    
#     if current_count == 0:
#         continue
        
#     if current_count >= TARGET_COUNT:
#         print(f"Skipping {class_name}: Already has {current_count} files (Target: {TARGET_COUNT})")
#         continue
        
#     print(f"Augmenting {class_name}... (Current: {current_count} -> Target: {TARGET_COUNT})")
    
#     files_needed = TARGET_COUNT - current_count
#     augmentations_generated = 0
    
#     while augmentations_generated < files_needed:
#         # Pick a random original file to modify
#         file_to_augment = random.choice(original_files)
#         file_path = os.path.join(class_dir, file_to_augment)
        
#         # Load the audio strictly as 16kHz mono
#         y, sr = librosa.load(file_path, sr=16000, mono=True)
        
#         # Pick a random augmentation technique
#         aug_type = random.choice(['noise', 'stretch_fast', 'stretch_slow', 'pitch_up', 'pitch_down'])
        
#         if aug_type == 'noise':
#             y_aug = add_noise(y)
#             suffix = "noise"
#         elif aug_type == 'stretch_fast':
#             y_aug = time_stretch(y, rate=1.15)
#             suffix = "stretchF"
#         elif aug_type == 'stretch_slow':
#             y_aug = time_stretch(y, rate=0.85)
#             suffix = "stretchS"
#         elif aug_type == 'pitch_up':
#             y_aug = pitch_shift(y, sr, n_steps=2)
#             suffix = "pitchU"
#         else:
#             y_aug = pitch_shift(y, sr, n_steps=-2)
#             suffix = "pitchD"
            
#         # 4. Save the new synthetic file
#         new_filename = f"aug_{augmentations_generated}_{suffix}_{file_to_augment}"
#         new_filepath = os.path.join(class_dir, new_filename)
        
#         sf.write(new_filepath, y_aug, sr)
#         augmentations_generated += 1

# print("\n================ AUGMENTATION COMPLETE ================")



import os
import random
import librosa
import numpy as np
import soundfile as sf

# 1. Hardcoded paths
base_dir = r"C:\Users\Tamanna Shaw\Downloads\IIIT-Dharwad\Project\ProjectCode\BidirectionalEmergencyCommunicationSystem\model1"
dataset_dir = os.path.join(base_dir, "dataset_final")

# Set the exact size of your Ambient_Noise class for perfect balance
TARGET_COUNT = 519

# 2. Define Augmentation Techniques
def add_noise(data, noise_factor=0.005):
    noise = np.random.randn(len(data))
    return data + noise_factor * noise

def time_stretch(data, rate):
    return librosa.effects.time_stretch(y=data, rate=rate)

def pitch_shift(data, sr, n_steps):
    return librosa.effects.pitch_shift(y=data, sr=sr, n_steps=n_steps)

print("Starting Data Augmentation Phase 2 (Target: 519)...")

class_names = [f for f in os.listdir(dataset_dir) if os.path.isdir(os.path.join(dataset_dir, f))]

for class_name in class_names:
    class_dir = os.path.join(dataset_dir, class_name)
    
    # Grab all files (including the ones we augmented in the first round)
    original_files = [f for f in os.listdir(class_dir) if f.endswith('.wav')]
    current_count = len(original_files)
    
    if current_count == 0 or current_count >= TARGET_COUNT:
        if current_count >= TARGET_COUNT:
             print(f"Skipping {class_name}: Already at {current_count} files.")
        continue
        
    print(f"Augmenting {class_name}... (Current: {current_count} -> Target: {TARGET_COUNT})")
    
    files_needed = TARGET_COUNT - current_count
    augmentations_generated = 0
    
    while augmentations_generated < files_needed:
        file_to_augment = random.choice(original_files)
        file_path = os.path.join(class_dir, file_to_augment)
        
        try:
            y, sr = librosa.load(file_path, sr=16000, mono=True)
            aug_type = random.choice(['noise', 'stretch_fast', 'stretch_slow', 'pitch_up', 'pitch_down'])
            
            if aug_type == 'noise':
                y_aug = add_noise(y)
                suffix = "noise2"
            elif aug_type == 'stretch_fast':
                y_aug = time_stretch(y, rate=1.15)
                suffix = "stretchF2"
            elif aug_type == 'stretch_slow':
                y_aug = time_stretch(y, rate=0.85)
                suffix = "stretchS2"
            elif aug_type == 'pitch_up':
                y_aug = pitch_shift(y, sr, n_steps=2)
                suffix = "pitchU2"
            else:
                y_aug = pitch_shift(y, sr, n_steps=-2)
                suffix = "pitchD2"
                
            new_filename = f"aug2_{augmentations_generated}_{suffix}_{file_to_augment}"
            new_filepath = os.path.join(class_dir, new_filename)
            
            sf.write(new_filepath, y_aug, sr)
            augmentations_generated += 1
        except Exception as e:
            pass # Skip corrupted files quietly

print("\n================ AUGMENTATION COMPLETE ================")