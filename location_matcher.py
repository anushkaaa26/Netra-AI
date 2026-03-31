# location_matcher.py — add this function at the bottom
from difflib import get_close_matches

LOCATIONS = [
    "Main Gate", "GH1", "GH2", "AB2",
    "MPH", "Mayuri", "UB", "Architecture", "LC", "AB1"
]

ALIASES = {
    "main gate": "Main Gate",
    "gate": "Main Gate",
    "entrance": "Main Gate",
    "gh1": "GH1",
    "girls hostel 1": "GH1",
    "hostel 1": "GH1",
    "gh2": "GH2",
    "girls hostel 2": "GH2",
    "hostel 2": "GH2",
    "ab2": "AB2",
    "academic block 2": "AB2",
    "block 2": "AB2",
    "mph": "MPH",
    "multipurpose hall": "MPH",
    "hall": "MPH",
    "mayuri": "Mayuri",
    "canteen": "Mayuri",
    "ub": "UB",
    "university building": "UB",
    "architecture": "Architecture",
    "arch": "Architecture",
    "lc": "LC",
    "lab complex": "LC",
    "lab": "LC",
    "laboratory": "LC",
    "laboratory complex": "LC",
    "labs": "LC",
    "ab1": "AB1",
    "ab1": "AB1",
    "academic block 1": "AB1",
    "block 1": "AB1",
}

def match_location(spoken: str):
    spoken = spoken.lower().strip()
    if spoken in ALIASES:
        return ALIASES[spoken]
    for alias, location in ALIASES.items():
        if alias in spoken:
            return location
    lower_locations = [l.lower() for l in LOCATIONS]
    matches = get_close_matches(spoken, lower_locations, n=1, cutoff=0.6)
    if matches:
        idx = lower_locations.index(matches[0])
        return LOCATIONS[idx]
    return None

# ✅ NEW — parses "main gate to LC" as a single phrase
def parse_start_destination(spoken: str):
    """
    If user says 'main gate to LC' in one breath,
    extract both start and destination.
    Returns (start, destination) or (None, None)
    """
    spoken = spoken.lower().strip()
    separators = [" to ", " towards ", " until ", " upto "]
    for sep in separators:
        if sep in spoken:
            parts = spoken.split(sep, 1)
            start = match_location(parts[0].strip())
            dest  = match_location(parts[1].strip())
            if start and dest:
                return start, dest
    return None, None