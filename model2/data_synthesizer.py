import pandas as pd
import random
from sklearn.model_selection import train_test_split

# 1. Load your existing file (Ensure it is in the same directory as your script)
df1 = pd.read_csv("./data/emergency_phrase_simplification_dataset_2000.csv")
df1_clean = df1.drop_duplicates().dropna()

# 2. Synthetic Generator to top up the dataset
intros = [
    "Please make sure to", "I need you to immediately", "Quickly", 
    "It is very important that you", "For your safety, please", 
    "You must", "Action required:", "Kindly", "Please", "Emergency:",
    "Attention:", "Warning:", "Right now, you need to", "Make sure you",
    "Without delay,"
]

actions_and_simplified = [
    ("take the left exit door and go down the stairs slowly", "Left. Exit. Stairs. Slowly."),
    ("cover your nose and mouth with a wet cloth and stay low to the ground", "Cover Nose. Stay Low."),
    ("leave your belongings behind and evacuate the building immediately", "Leave Belongings. Evacuate Now."),
    ("find a safe place to hide and stay quiet until help arrives", "Hide. Stay Quiet."),
    ("apply direct pressure to the wound and elevate the injured area", "Apply Pressure. Elevate Wound."),
    ("call an ambulance and wait outside for them to arrive", "Call Ambulance. Wait Outside."),
    ("drop to the floor, take cover under a sturdy table, and hold on", "Drop. Cover. Hold On."),
    ("do not use the elevators, use the emergency fire stairs", "No Elevators. Use Stairs."),
    ("move away from the windows and find a secure room", "Away From Windows. Secure Room."),
    ("turn off the main gas valve and evacuate the premises", "Turn Off Gas. Evacuate."),
    ("lock the doors, turn off the lights, and remain silent", "Lock Doors. Lights Off. Remain Silent."),
    ("use the fire extinguisher on the base of the flames", "Extinguish Fire. Aim at Base."),
    ("stay away from electrical outlets and avoid using wired devices", "Avoid Outlets. No Wired Devices."),
    ("check for breathing and begin CPR if necessary", "Check Breathing. Start CPR."),
    ("do not drink the tap water, use bottled water instead", "No Tap Water. Use Bottled."),
    ("move to higher ground immediately to avoid the floodwaters", "Move Higher. Avoid Flood."),
    ("stay inside your vehicle and wait for emergency responders", "Stay In Vehicle. Wait."),
    ("crawl under the smoke to reach the nearest safe exit", "Crawl Under Smoke. Find Exit."),
    ("secure all loose objects and stay away from glass panels", "Secure Objects. Avoid Glass."),
    ("activate the fire alarm on your way out of the corridor", "Activate Alarm. Exit Corridor.")
]

fillers = [
    " as soon as possible.", " right now.", " without panicking.", 
    " to ensure your safety.", " and help others if you can.", ".",
    " immediately.", " before the situation worsens.", " carefully.",
    " while waiting for responders.", " and stay calm.", " as instructed."
]

synthetic_data = []

# Generate enough permutations to guarantee >= 2000 total unique rows
for _ in range(3500):
    intro = random.choice(intros)
    action_pair = random.choice(actions_and_simplified)
    filler = random.choice(fillers)
    
    original = f"{intro} {action_pair[0]}{filler}".strip().capitalize()
    simplified = action_pair[1]
    synthetic_data.append({"original_instruction": original, "simplified_phrase": simplified})

# 3. Combine original clean data with synthetic data
df_synthetic = pd.DataFrame(synthetic_data)
combined_df = pd.concat([df1_clean, df_synthetic], ignore_index=True)

# 4. Deduplicate the entire combined dataset to ensure absolute uniqueness
final_clean_df = combined_df.drop_duplicates().dropna()

# 5. Format inputs specifically for the FLAN-T5 Model 
final_clean_df["input_text"] = "Simplify this emergency instruction into concise, actionable phrases: " + final_clean_df["original_instruction"]
final_dataset = final_clean_df[["input_text", "simplified_phrase"]]

# 6. Split into Training and Testing sets (85% Train, 15% Test)
train_df, test_df = train_test_split(final_dataset, test_size=0.15, random_state=42)

# 7. Save to CSV directly in your working directory
train_df.to_csv("train_emergency_data_final.csv", index=False)
test_df.to_csv("test_emergency_data_final.csv", index=False)

print(f"Success! Training set saved with {len(train_df)} rows.")
print(f"Success! Testing set saved with {len(test_df)} rows.")

# --- GOOGLE COLAB USERS ONLY ---
# If you are running this in Google Colab, uncomment the three lines below 
# to automatically trigger the file downloads to your local computer:

# from google.colab import files
# files.download("train_emergency_data_final.csv")
# files.download("test_emergency_data_final.csv")