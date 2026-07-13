"""
templates.py

Contains all sentence templates used to generate emergency instructions.

Each template has placeholders that will be replaced by words from
vocabulary.py.
"""

# ============================================================
# FIRE TEMPLATES
# ============================================================

FIRE_TEMPLATES = [

    "Please evacuate the {place} immediately using the {exit}.",

    "There is {hazard} inside the {place}. Move toward the {exit}.",

    "{hazard} has been reported in the {floor} of the {place}. Leave immediately.",

    "Heavy smoke has filled the {place}. Stay low and use the {exit}.",

    "Leave the {place} immediately. Do not use the elevator.",

    "Smoke is spreading throughout the {place}. Cover your nose and proceed to the {exit}.",

    "Everyone must leave the {place} through the {exit}.",

    "Fire has broken out inside the {place}. Stay calm and evacuate immediately.",

    "Avoid the smoke and leave using the {exit}.",

    "Use the staircase instead of the elevator while leaving the {place}.",

    "Help the {people} while evacuating the {place}.",

    "Keep away from the flames and proceed toward the {exit}.",

    "Emergency teams are responding. Leave the {place} immediately.",

    "Do not return inside the {place} until authorities declare it safe.",

    "Remain calm and follow evacuation instructions through the {exit}."

]

# ============================================================
# FLOOD TEMPLATES
# ============================================================

FLOOD_TEMPLATES = [

    "Flood water is rising near the {place}. Move to higher ground.",

    "Leave the {place} immediately because flood water is approaching.",

    "Avoid walking through flood water.",

    "Switch off electricity before leaving the {place}.",

    "Move everyone toward higher ground immediately.",

    "Heavy rainfall has caused flooding around the {place}.",

    "Do not drive through flooded roads.",

    "Stay away from open drains and flooded streets.",

    "Rescue teams are arriving. Stay in a safe location.",

    "Move the {people} to higher ground immediately.",

    "Avoid crossing moving water.",

    "The river level is increasing rapidly. Evacuate immediately.",

    "Take only essential belongings before leaving.",

    "Proceed to the designated shelter."

]

# ============================================================
# EARTHQUAKE TEMPLATES
# ============================================================

EARTHQUAKE_TEMPLATES = [

    "An earthquake is occurring. Drop, cover and hold.",

    "Stay away from windows during the earthquake.",

    "Protect your head and neck immediately.",

    "Do not use elevators after the earthquake.",

    "Leave the {place} only after shaking stops.",

    "Move to an open area away from buildings.",

    "Watch for falling objects.",

    "Remain calm and follow emergency instructions.",

    "After evacuation proceed to the assembly point.",

    "Check for injuries after reaching safety.",

    "Expect aftershocks and stay alert.",

    "Help the {people} while evacuating."

]

# ============================================================
# EXPLOSION TEMPLATES
# ============================================================

EXPLOSION_TEMPLATES = [

    "An explosion has occurred inside the {place}. Move away immediately.",

    "Take cover from flying debris.",

    "Do not approach the damaged building.",

    "Leave the area immediately.",

    "Emergency responders are on the way.",

    "Stay away from broken glass.",

    "Use the safest available exit.",

    "Keep clear of damaged structures.",

    "Remain outside until authorities allow entry.",

    "Move everyone away from the explosion site."

]

# ============================================================
# CHEMICAL LEAK
# ============================================================

CHEMICAL_TEMPLATES = [

    "A chemical leak has been detected inside the {place}.",

    "Cover your nose and mouth immediately.",

    "Leave the contaminated area.",

    "Avoid inhaling toxic fumes.",

    "Move upwind from the leak.",

    "Do not touch spilled chemicals.",

    "Close doors while leaving the area.",

    "Wait for emergency responders.",

    "Stay away from the affected zone.",

    "Use the {exit} while leaving."

]

# ============================================================
# MEDICAL EMERGENCY
# ============================================================

MEDICAL_TEMPLATES = [

    "Someone has suffered a {medical_event}.",

    "Call an ambulance immediately.",

    "Keep the patient still.",

    "Provide first aid if trained.",

    "Do not crowd around the patient.",

    "Allow medical staff to work.",

    "Clear the surrounding area.",

    "Help the injured person remain calm.",

    "Guide emergency responders to the patient.",

    "Stay nearby until help arrives."

]

# ============================================================
# GUNSHOT
# ============================================================

GUNSHOT_TEMPLATES = [

    "Gunshots have been reported.",

    "Run if it is safe.",

    "Hide if escape is impossible.",

    "Remain silent while hiding.",

    "Lock the doors.",

    "Turn off lights.",

    "Stay away from windows.",

    "Call the police when safe.",

    "Keep your phone silent.",

    "Wait for police instructions."

]

# ============================================================
# ROAD ACCIDENT
# ============================================================

ROAD_ACCIDENT_TEMPLATES = [

    "A road accident has occurred nearby.",

    "Call an ambulance immediately.",

    "Do not move the injured person.",

    "Keep traffic away from the accident.",

    "Stay clear of leaking fuel.",

    "Wait for emergency responders.",

    "Provide first aid if trained.",

    "Keep bystanders away.",

    "Remain calm.",

    "Stay in a safe location."

]

# ============================================================
# CROWD PANIC
# ============================================================

CROWD_PANIC_TEMPLATES = [

    "Avoid pushing others.",

    "Move slowly toward the exit.",

    "Stay calm.",

    "Follow security instructions.",

    "Keep moving steadily.",

    "Help the {people}.",

    "Do not run unnecessarily.",

    "Avoid blocked exits.",

    "Proceed toward the nearest safe area.",

    "Remain patient."

]

# ============================================================
# GENERAL EMERGENCY
# ============================================================

GENERAL_TEMPLATES = [

    "Remain calm.",

    "Follow official instructions.",

    "Move toward the designated safe area.",

    "Wait for emergency responders.",

    "Stay alert.",

    "Keep emergency exits clear.",

    "Do not spread rumors.",

    "Help the {people}.",

    "Leave dangerous areas immediately.",

    "Stay together until further instructions."

]

# ============================================================
# DICTIONARY
# ============================================================

SCENARIO_TEMPLATES = {

    "fire": FIRE_TEMPLATES,

    "flood": FLOOD_TEMPLATES,

    "earthquake": EARTHQUAKE_TEMPLATES,

    "explosion": EXPLOSION_TEMPLATES,

    "chemical": CHEMICAL_TEMPLATES,

    "medical": MEDICAL_TEMPLATES,

    "gunshot": GUNSHOT_TEMPLATES,

    "road_accident": ROAD_ACCIDENT_TEMPLATES,

    "crowd_panic": CROWD_PANIC_TEMPLATES,

    "general": GENERAL_TEMPLATES

}