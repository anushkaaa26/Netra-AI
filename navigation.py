# navigation.py
from tts import speak

campus_graph = {
    "Main Gate":    ["GH1", "MPH"],
    "GH1":          ["Main Gate", "GH2"],
    "GH2":          ["GH1", "AB2"],
    "AB2":          ["GH2"],
    "MPH":          ["Main Gate", "Mayuri"],
    "Mayuri":       ["MPH", "UB", "AB1"],
    "UB":           ["Mayuri", "Architecture"],
    "Architecture": ["UB", "LC"],
    "LC":           ["Architecture"],
    "AB1":          ["Mayuri"]
}

# Turn-by-turn directions for each edge
DIRECTIONS = {
    ("Main Gate", "GH1"):        "Go straight, turn left, then turn right, then go straight. GH1 will be on your right side.",
    ("GH1", "Main Gate"):        "Go straight, turn left, then turn right, and continue straight to Main Gate.",
    ("Main Gate", "MPH"):        "Go a little straight, then turn right towards MPH.",
    ("MPH", "Main Gate"):        "Turn left and go straight back to Main Gate.",
    ("GH1", "GH2"):              "Go straight ahead. GH2 is just next to GH1.",
    ("GH2", "GH1"):              "Go straight back. GH1 is right next to you.",
    ("GH2", "AB2"):              "Go a little straight, then turn right towards AB2.",
    ("AB2", "GH2"):              "Turn left and go straight back to GH2.",
    ("MPH", "Mayuri"):           "Go straight, then turn left, then turn right towards Mayuri.",
    ("Mayuri", "MPH"):           "Turn left, then right, then straight back to MPH.",
    ("Mayuri", "UB"):            "Take the next right towards UB.",
    ("UB", "Mayuri"):            "Turn around and go straight back to Mayuri.",
    ("Mayuri", "AB1"):           "Go straight forward, no turns. AB1 is straight ahead.",
    ("AB1", "Mayuri"):           "Go straight back to Mayuri, no turns.",
    ("UB", "Architecture"):      "Turn right and go straight. Architecture block is on your right side.",
    ("Architecture", "UB"):      "Turn left and go straight back to UB.",
    ("Architecture", "LC"):      "Go straight ahead. Lab Complex will be on your left side.",
    ("LC", "Architecture"):      "Turn around, Lab Complex is behind you, go straight to Architecture.",
}

def find_path(graph, start, end):
    queue = [(start, [start])]
    visited = set()
    while queue:
        node, path = queue.pop(0)
        if node == end:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))
    return []

def generate_instructions(path):
    """Generate step-by-step turn-by-turn instructions."""
    instructions = []
    for i in range(len(path) - 1):
        curr = path[i]
        nxt  = path[i + 1]
        direction = DIRECTIONS.get((curr, nxt), f"Proceed to {nxt}")
        instructions.append(f"From {curr}: {direction}")
    return instructions

def get_route_summary(path):
    """
    Speaks the full route overview before starting step by step.
    e.g. 'You will go from Main Gate → MPH → Mayuri → UB → Architecture → LC'
    """
    route = " then ".join(path)
    total_steps = len(path) - 1
    return f"Your route has {total_steps} steps. You will pass through: {route}."

def start_navigation(start, destination):
    if start == destination:
        return ["You are already at your destination"], []
    path = find_path(campus_graph, start, destination)
    if not path:
        return ["No path found between these locations"], []
    instructions = generate_instructions(path)
    summary = get_route_summary(path)
    return instructions, summary