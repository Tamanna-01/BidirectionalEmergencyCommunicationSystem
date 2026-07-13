"""
vocabulary.py

Contains all vocabulary used for generating emergency instructions.
"""

# ============================================================
# LOCATIONS
# ============================================================

PLACES = [
    "building",
    "office",
    "shopping mall",
    "hospital",
    "school",
    "college",
    "university",
    "airport",
    "railway station",
    "metro station",
    "bus station",
    "warehouse",
    "factory",
    "parking lot",
    "cinema",
    "hotel",
    "apartment",
    "library",
    "restaurant",
    "supermarket",
    "bank",
    "laboratory",
    "construction site",
    "sports stadium",
    "community hall"
]

# ============================================================
# EXITS
# ============================================================

EXITS = [
    "nearest exit",
    "front exit",
    "rear exit",
    "side exit",
    "emergency exit",
    "fire exit",
    "main entrance",
    "staircase",
    "east exit",
    "west exit",
    "north exit",
    "south exit"
]

# ============================================================
# FLOORS
# ============================================================

FLOORS = [
    "ground floor",
    "first floor",
    "second floor",
    "third floor",
    "top floor",
    "basement"
]

# ============================================================
# EMERGENCY HAZARDS
# ============================================================

HAZARDS = [
    "fire",
    "heavy smoke",
    "thick smoke",
    "gas leak",
    "chemical leak",
    "chemical spill",
    "explosion",
    "electrical fire",
    "earthquake",
    "flood",
    "gunfire",
    "bomb threat",
    "building collapse",
    "toxic fumes",
    "short circuit"
]

# ============================================================
# PEOPLE
# ============================================================

PEOPLE = [
    "children",
    "elderly people",
    "elderly",
    "disabled people",
    "injured people",
    "patients",
    "visitors",
    "everyone",
    "staff",
    "workers",
    "students",
    "customers"
]

# ============================================================
# BODY PARTS
# ============================================================

BODY_PARTS = [
    "nose",
    "mouth",
    "head",
    "face"
]

# ============================================================
# ACTION VERBS
# ============================================================

ACTIONS = [
    "leave",
    "evacuate",
    "exit",
    "move",
    "proceed",
    "walk",
    "run",
    "escape"
]

# ============================================================
# SAFE LOCATIONS
# ============================================================

SAFE_PLACES = [
    "assembly point",
    "safe zone",
    "open ground",
    "higher ground",
    "outside",
    "designated shelter",
    "parking area"
]

# ============================================================
# EMERGENCY SERVICES
# ============================================================

SERVICES = [
    "ambulance",
    "fire department",
    "police",
    "emergency services",
    "security",
    "medical team"
]

# ============================================================
# WARNING PHRASES
# ============================================================

WARNINGS = [
    "stay calm",
    "do not panic",
    "remain calm",
    "act quickly",
    "avoid pushing",
    "stay alert"
]

# ============================================================
# PROTECTIVE ACTIONS
# ============================================================

PROTECTIVE_ACTIONS = [
    "cover your nose",
    "cover your mouth",
    "stay low",
    "take cover",
    "avoid elevators",
    "use stairs",
    "keep distance",
    "move away",
    "stay outside",
    "avoid windows"
]

# ============================================================
# MEDICAL EVENTS
# ============================================================

MEDICAL_EVENTS = [
    "heart attack",
    "person unconscious",
    "serious injury",
    "bleeding",
    "burn injury",
    "medical emergency"
]

# ============================================================
# FLOOD ACTIONS
# ============================================================

FLOOD_ACTIONS = [
    "move to higher ground",
    "avoid flood water",
    "switch off electricity",
    "stay away from drains",
    "leave low-lying areas"
]

# ============================================================
# EARTHQUAKE ACTIONS
# ============================================================

EARTHQUAKE_ACTIONS = [
    "drop",
    "cover",
    "hold on",
    "stay away from windows",
    "protect your head"
]

# ============================================================
# FIRE ACTIONS
# ============================================================

FIRE_ACTIONS = [
    "use fire exit",
    "stay low",
    "cover nose",
    "leave immediately",
    "avoid smoke"
]

# ============================================================
# CHEMICAL LEAK ACTIONS
# ============================================================

CHEMICAL_ACTIONS = [
    "move upwind",
    "avoid inhalation",
    "cover nose",
    "leave area",
    "avoid contact"
]

# ============================================================
# ROAD ACCIDENT ACTIONS
# ============================================================

ROAD_ACTIONS = [
    "call ambulance",
    "do not move victim",
    "control traffic",
    "stay away",
    "wait for medical team"
]

# ============================================================
# GUNFIRE ACTIONS
# ============================================================

GUNSHOT_ACTIONS = [
    "run",
    "hide",
    "stay silent",
    "call police",
    "take cover"
]

# ============================================================
# CROWD PANIC ACTIONS
# ============================================================

CROWD_ACTIONS = [
    "avoid pushing",
    "move sideways",
    "stay calm",
    "follow instructions",
    "keep moving"
]

# ============================================================
# BUILDING COLLAPSE ACTIONS
# ============================================================

COLLAPSE_ACTIONS = [
    "move away",
    "do not enter",
    "wait for rescue",
    "stay clear",
    "avoid debris"
]

# ============================================================
# SYNONYMS
# Used to create diverse input sentences
# ============================================================

ACTION_SYNONYMS = {
    "leave": [
        "leave",
        "exit",
        "evacuate",
        "move out of",
        "get out of"
    ],

    "move": [
        "move",
        "proceed",
        "walk",
        "head toward"
    ],

    "run": [
        "run",
        "escape",
        "move quickly"
    ]
}

# ============================================================
# URGENCY WORDS
# ============================================================

URGENCY = [
    "immediately",
    "right now",
    "as soon as possible",
    "without delay",
    "quickly",
    "at once"
]

# ============================================================
# SPEECH-LIKE STARTERS
# Used for STT-style transcripts
# ============================================================

SPEECH_STARTERS = [
    "everyone",
    "listen",
    "attention everyone",
    "please",
    "quick",
    "hurry",
    "be careful",
    "warning"
]

# ============================================================
# RANDOM FILLER WORDS
# Makes speech transcripts realistic
# ============================================================

FILLERS = [
    "uh",
    "please",
    "everyone",
    "listen",
    "okay",
    "come on",
    "quickly"
]