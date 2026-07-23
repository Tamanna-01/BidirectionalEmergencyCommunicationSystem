import os
import shutil

# Hardcoded paths based on your terminal output
base_dir = r"C:\Users\Tamanna Shaw\Downloads\IIIT-Dharwad\Project\ProjectCode\BidirectionalEmergencyCommunicationSystem"
source_dir = os.path.join(base_dir, "emergency_audio_dataset")
target_dir = os.path.join(base_dir, "model1\dataset_final")

# Mapping AudioSet subfolders to main emergency classes
class_mapping = {
    "Alarm": [
        "Alarm", 
        "Car alarm", 
        "Smoke detector, smoke alarm", 
        "Alarm clock", 
        "Buzzer"
    ],
    "Siren": [
        "Siren", 
        "Ambulance (siren)", 
        "Fire engine, fire truck (siren)", 
        "Civil defense siren", 
        "Police car (siren)"
    ],
    "Explosion": [
        "Explosion", 
        "Firecracker", 
        "Artillery fire", 
        "Eruption"
    ],
    "Gunshot": [
        "Gunshot, gunfire", 
        "Fusillade", 
        "Cap gun", 
        "Machine gun"
    ],
    "Scream_Yell": [
        "Screaming", 
        "Yell", 
        "Groan", 
        "Wail, moan"
    ],
    "Emergency_Vehicle": [
        "Emergency vehicle"
    ],
    "Ambient_Noise": [
        "Speech", 
        "Vehicle", 
        "Outside, rural or natural", 
        "Motorcycle", 
        "Traffic noise, roadway noise", 
        "Motor vehicle (road)", 
        "Truck", 
        "Bus", 
        "Crowd", 
        "Bird", 
        "Silence", 
        "Walk, footsteps", 
        "Run", 
        "Idling"
    ]
}

# Create target directory
os.makedirs(target_dir, exist_ok=True)

copied_counts = {key: 0 for key in class_mapping.keys()}

print("Starting dataset reorganization...")

for master_class, subfolders in class_mapping.items():
    master_class_path = os.path.join(target_dir, master_class)
    os.makedirs(master_class_path, exist_ok=True)
    
    for subfolder in subfolders:
        subfolder_path = os.path.join(source_dir, subfolder)
        
        if os.path.exists(subfolder_path):
            files = [f for f in os.listdir(subfolder_path) if f.endswith('.wav')]
            for file_name in files:
                src_file = os.path.join(subfolder_path, file_name)
                # Rename file slightly to prevent overwriting files with the same name across subfolders
                clean_subfolder_name = subfolder.replace(",", "").replace(" ", "_")
                dst_file = os.path.join(master_class_path, f"{clean_subfolder_name}_{file_name}")
                
                shutil.copy2(src_file, dst_file)
                copied_counts[master_class] += 1

print("\n================ DATASET SUMMARY ================")
for cls, count in copied_counts.items():
    print(f"Class: {cls:<20} Total Files: {count}")
print("=================================================\n")
print(f"All valid audio files copied successfully to:\n{target_dir}")