"""
utils.py

Helper functions for generating emergency instruction datasets.
"""

import random
import re

from vocabulary import *

# ============================================================
# RANDOM PLACEHOLDER VALUES
# ============================================================

def get_random_values():

    return {

        "place": random.choice(PLACES),

        "exit": random.choice(EXITS),

        "floor": random.choice(FLOORS),

        "hazard": random.choice(HAZARDS),

        "people": random.choice(PEOPLE),

        "medical_event": random.choice(MEDICAL_EVENTS),

        "safe_place": random.choice(SAFE_PLACES),

        "service": random.choice(SERVICES),

        "urgency": random.choice(URGENCY),

    }


# ============================================================
# FILL TEMPLATE
# ============================================================

def fill_template(template):

    values = get_random_values()

    return template.format(**values)


# ============================================================
# COMBINE MULTIPLE TEMPLATES
# ============================================================

def combine_templates(template_list,
                      min_sentences=1,
                      max_sentences=4):

    n = random.randint(min_sentences,
                       max_sentences)

    selected = random.sample(template_list, n)

    completed = []

    for t in selected:

        completed.append(fill_template(t))

    return " ".join(completed)


# ============================================================
# FORMAL VERSION
# ============================================================

def formal_text(text):

    return text


# ============================================================
# SPEECH VERSION
# ============================================================

def speech_text(text):

    words = text.split()

    output = []

    if random.random() < 0.5:

        output.append(random.choice(SPEECH_STARTERS))

    for word in words:

        if random.random() < 0.05:

            output.append(random.choice(FILLERS))

        output.append(word)

    sentence = " ".join(output)

    sentence = sentence.replace(".", "")

    sentence = sentence.replace(",", "")

    return sentence


# ============================================================
# PANIC VERSION
# ============================================================

def panic_text(text):

    text = speech_text(text)

    words = text.split()

    important = []

    for w in words:

        if len(w) > 3:

            important.append(w.upper())

    if len(important) > 10:

        important = important[:10]

    return " ! ".join(important)


# ============================================================
# SIMPLE TARGET GENERATOR
# ============================================================

def generate_target(text):

    text = text.lower()

    target = []

    # --------------------------------------------------------

    if "smoke" in text:

        target.append("SMOKE PRESENT")

    if "fire" in text:

        target.append("FIRE ALERT")

    if "explosion" in text:

        target.append("EXPLOSION")

    if "chemical" in text:

        target.append("CHEMICAL LEAK")

    if "gas leak" in text:

        target.append("GAS LEAK")

    if "flood" in text:

        target.append("FLOOD ALERT")

    if "earthquake" in text:

        target.append("EARTHQUAKE")

    if "gunshot" in text or "gunfire" in text:

        target.append("GUNFIRE")

    # --------------------------------------------------------

    if "stay low" in text:

        target.append("STAY LOW")

    if "cover your nose" in text:

        target.append("COVER NOSE")

    if "cover your mouth" in text:

        target.append("COVER MOUTH")

    if "avoid elevators" in text:

        target.append("NO ELEVATOR")

    if "use stairs" in text:

        target.append("USE STAIRS")

    if "take cover" in text:

        target.append("TAKE COVER")

    if "hide" in text:

        target.append("HIDE")

    if "run" in text:

        target.append("RUN")

    # --------------------------------------------------------

    if "ambulance" in text:

        target.append("CALL AMBULANCE")

    if "police" in text:

        target.append("CALL POLICE")

    if "fire department" in text:

        target.append("CALL FIRE DEPARTMENT")

    # --------------------------------------------------------

    if "higher ground" in text:

        target.append("MOVE HIGHER")

    if "assembly point" in text:

        target.append("GO ASSEMBLY POINT")

    if "safe zone" in text:

        target.append("GO SAFE ZONE")

    # --------------------------------------------------------

    if "leave" in text:

        target.append("EXIT BUILDING")

    if "evacuate" in text:

        target.append("EVACUATE")

    if "exit" in text:

        target.append("USE EXIT")

    # --------------------------------------------------------

    if "elderly" in text:

        target.append("HELP ELDERLY")

    if "children" in text:

        target.append("HELP CHILDREN")

    if "injured" in text:

        target.append("HELP INJURED")

    if "disabled" in text:

        target.append("HELP DISABLED")

    # --------------------------------------------------------

    final = []

    for item in target:

        if item not in final:

            final.append(item)

    return ". ".join(final)


# ============================================================
# CLEAN TEXT
# ============================================================

def clean_text(text):

    text = re.sub(r"\s+", " ", text)

    text = text.strip()

    return text


# ============================================================
# VALIDATE SAMPLE
# ============================================================

def valid_sample(inp,
                 target):

    if len(inp) < 20:

        return False

    if len(target) == 0:

        return False

    return True


# ============================================================
# REMOVE DUPLICATES
# ============================================================

def remove_duplicates(samples):

    seen = set()

    cleaned = []

    for row in samples:

        if row["input"] not in seen:

            seen.add(row["input"])

            cleaned.append(row)

    return cleaned