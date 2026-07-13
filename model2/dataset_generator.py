"""
dataset_generator.py

Main script to generate the Emergency Phrase Simplification Dataset.

Author: Tamanna Shaw
"""

import os
import random
import pandas as pd

from templates import SCENARIO_TEMPLATES
from utils import (
    combine_templates,
    formal_text,
    speech_text,
    panic_text,
    clean_text,
    valid_sample,
    remove_duplicates
)

# ============================================================
# CONFIGURATION
# ============================================================

TOTAL_SAMPLES = 2000

OUTPUT_FOLDER = "output"

OUTPUT_FILE = os.path.join(
    OUTPUT_FOLDER,
    "emergency_dataset.csv"
)

# Percentage of each input style

FORMAL_RATIO = 0.40
SPEECH_RATIO = 0.40
PANIC_RATIO = 0.20

random.seed(42)

# ============================================================
# CONTEXT-AWARE TARGET GENERATOR
# ============================================================

def generate_context_target(text):

    text_lower = text.lower()

    target = []

    # -------------------------------------------------------
    # Hazards
    # -------------------------------------------------------

    if "fire" in text_lower:
        target.append("FIRE ALERT")

    if "smoke" in text_lower:
        target.append("SMOKE PRESENT")

    if "explosion" in text_lower:
        target.append("EXPLOSION")

    if "chemical" in text_lower:
        target.append("CHEMICAL LEAK")

    if "gas leak" in text_lower:
        target.append("GAS LEAK")

    if "flood" in text_lower:
        target.append("FLOOD ALERT")

    if "earthquake" in text_lower:
        target.append("EARTHQUAKE")

    if "gunshot" in text_lower or "gunfire" in text_lower:
        target.append("GUNFIRE")

    # -------------------------------------------------------
    # Place
    # -------------------------------------------------------

    places = [
        "hospital",
        "school",
        "office",
        "building",
        "shopping mall",
        "airport",
        "warehouse",
        "factory",
        "restaurant",
        "hotel",
        "bank",
        "library",
        "college",
        "metro station",
        "railway station"
    ]

    for place in places:

        if place in text_lower:

            target.append(
                f"EXIT {place.upper()}"
            )

            break

    # -------------------------------------------------------
    # Exit
    # -------------------------------------------------------

    exits = [
        "fire exit",
        "emergency exit",
        "front exit",
        "rear exit",
        "side exit",
        "staircase"
    ]

    for e in exits:

        if e in text_lower:

            target.append(
                f"USE {e.upper()}"
            )

            break

    # -------------------------------------------------------
    # Actions
    # -------------------------------------------------------

    if "stay low" in text_lower:
        target.append("STAY LOW")

    if "cover your nose" in text_lower:
        target.append("COVER NOSE")

    if "cover your mouth" in text_lower:
        target.append("COVER MOUTH")

    if "avoid elevators" in text_lower:
        target.append("NO ELEVATOR")

    if "use stairs" in text_lower:
        target.append("USE STAIRS")

    if "take cover" in text_lower:
        target.append("TAKE COVER")

    if "run" in text_lower:
        target.append("RUN")

    if "hide" in text_lower:
        target.append("HIDE")

    if "move to higher ground" in text_lower:
        target.append("MOVE HIGHER")

    # -------------------------------------------------------
    # Emergency Services
    # -------------------------------------------------------

    if "ambulance" in text_lower:
        target.append("CALL AMBULANCE")

    if "police" in text_lower:
        target.append("CALL POLICE")

    if "fire department" in text_lower:
        target.append("CALL FIRE DEPARTMENT")

    # -------------------------------------------------------
    # Help Groups
    # -------------------------------------------------------

    if "elderly" in text_lower:
        target.append("HELP ELDERLY")

    if "children" in text_lower:
        target.append("HELP CHILDREN")

    if "injured" in text_lower:
        target.append("HELP INJURED")

    if "disabled" in text_lower:
        target.append("HELP DISABLED")

    # -------------------------------------------------------

    final = []

    for t in target:

        if t not in final:

            final.append(t)

    return ". ".join(final)


# ============================================================
# INPUT STYLE
# ============================================================

def create_input_style(text):

    r = random.random()

    if r < FORMAL_RATIO:

        return formal_text(text)

    elif r < FORMAL_RATIO + SPEECH_RATIO:

        return speech_text(text)

    else:

        return panic_text(text)


# ============================================================
# DATASET GENERATION
# ============================================================

def build_dataset():

    samples = []

    scenarios = list(
        SCENARIO_TEMPLATES.keys()
    )

    while len(samples) < TOTAL_SAMPLES:

        scenario = random.choice(
            scenarios
        )

        template_list = SCENARIO_TEMPLATES[
            scenario
        ]

        instruction = combine_templates(
            template_list,
            min_sentences=1,
            max_sentences=4
        )

        instruction = clean_text(
            instruction
        )

        model_input = create_input_style(
            instruction
        )

        target = generate_context_target(
            instruction
        )

        if valid_sample(
            model_input,
            target
        ):

            samples.append({

                "scenario": scenario,

                "input": model_input,

                "target": target

            })

    samples = remove_duplicates(
        samples
    )

    return pd.DataFrame(samples)


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    os.makedirs(
        OUTPUT_FOLDER,
        exist_ok=True
    )

    df = build_dataset()

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("=" * 50)
    print("Dataset Generated Successfully")
    print("=" * 50)
    print(f"Total Samples : {len(df)}")
    print(f"Saved At      : {OUTPUT_FILE}")

    print("\nSample Rows\n")

    print(df.head())