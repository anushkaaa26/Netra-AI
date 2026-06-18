"""
streamlit_demo.py
------------------
Interactive demo/visualizer for Netra-AI's campus navigation logic.

Why this exists:
Netra-AI's full pipeline needs a microphone, camera, and trained YOLO
models to run end-to-end. That makes it hard for anyone browsing the
repo to actually see what the navigation system does. This demo
isolates the navigation + location-matching logic (no hardware needed)
so it can be tried directly in the browser.

This file does NOT modify any existing module. It only imports from
navigation.py and location_matcher.py.
"""

import sys
import types
import time

import streamlit as st
import streamlit.components.v1 as components

# navigation.py does `from tts import speak`, and tts.py shells out to
# macOS `say` / pyttsx3. Irrelevant for a text/visual demo and would
# crash on platforms without those deps — stub it before importing.
if "tts" not in sys.modules:
    fake_tts = types.ModuleType("tts")
    fake_tts.speak = lambda text: None
    sys.modules["tts"] = fake_tts

from navigation import campus_graph, find_path, generate_instructions, get_route_summary
from location_matcher import LOCATIONS, match_location, parse_start_destination

st.set_page_config(page_title="Netra-AI · Navigation", page_icon="👁", layout="centered")

# ----------------------------------------------------------------
# Visual identity
# Ink navy + warm amber (a beacon/guide-light feel), serif display
# type for warmth, set against a quiet utility sans for UI chrome.
# ----------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter:wght@400;500;600&display=swap');

:root {
    --ink: #1a1f2e;
    --ink-soft: #232a3d;
    --paper: #f3efe6;
    --amber: #e8a849;
    --amber-dim: #c8923f;
    --coral: #e2725b;
    --slate: #8891a3;
}

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.stApp {
    background: var(--ink);
    color: var(--paper);
}

/* Kill default Streamlit chrome that screams "template" */
header[data-testid="stHeader"] { background: transparent; }
.block-container { padding-top: 2.5rem; max-width: 700px; }
footer { visibility: hidden; }
#MainMenu { visibility: hidden; }

/* Eyebrow + headline */
.eyebrow {
    font-family: 'Inter', sans-serif;
    font-size: 0.78rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: var(--amber);
    font-weight: 600;
    margin-bottom: 0.4rem;
}
.headline {
    font-family: 'Fraunces', serif;
    font-size: 2.6rem;
    font-weight: 500;
    line-height: 1.1;
    color: var(--paper);
    margin-bottom: 0.3rem;
}
.subhead {
    color: var(--slate);
    font-size: 1rem;
    line-height: 1.5;
    margin-bottom: 2.2rem;
    max-width: 540px;
}

/* The "spoken sentence" route builder */
.sentence-row {
    font-family: 'Fraunces', serif;
    font-size: 1.4rem;
    color: var(--paper);
    display: flex;
    align-items: center;
    gap: 0.5rem;
    flex-wrap: wrap;
    margin-bottom: 0.2rem;
}

div[data-baseweb="select"] {
    border-radius: 999px !important;
}
div[data-baseweb="select"] > div {
    background: var(--ink-soft) !important;
    border: 1.5px solid var(--amber-dim) !important;
    border-radius: 999px !important;
    color: var(--amber) !important;
    font-family: 'Fraunces', serif !important;
    font-weight: 500 !important;
    padding-left: 0.4rem;
}
div[data-baseweb="select"] svg { fill: var(--amber) !important; }

/* Primary button -> beacon */
.stButton > button {
    background: var(--amber) !important;
    color: var(--ink) !important;
    border: none !important;
    border-radius: 999px !important;
    font-weight: 600 !important;
    padding: 0.6rem 1.8rem !important;
    font-family: 'Inter', sans-serif !important;
    letter-spacing: 0.01em;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
    box-shadow: 0 4px 14px rgba(232, 168, 73, 0.0);
}
.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 20px rgba(232, 168, 73, 0.25);
}

/* Route summary strip */
.route-summary {
    border-left: 3px solid var(--amber);
    padding: 0.7rem 1rem;
    background: var(--ink-soft);
    color: var(--paper);
    font-size: 0.95rem;
    border-radius: 0 10px 10px 0;
    margin: 1.4rem 0 1.6rem 0;
}

/* Step cards */
.step-card {
    display: flex;
    gap: 0.9rem;
    padding: 0.85rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.07);
}
.step-num {
    font-family: 'Fraunces', serif;
    font-size: 1.1rem;
    color: var(--amber);
    min-width: 1.6rem;
}
.step-text { color: var(--paper); font-size: 0.98rem; line-height: 1.5; padding-top: 0.05rem; }
.step-from { color: var(--slate); font-size: 0.8rem; display: block; margin-bottom: 0.1rem; }

/* Section divider label */
.section-label {
    font-size: 0.78rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--slate);
    margin: 2.6rem 0 0.9rem 0;
    display: flex;
    align-items: center;
    gap: 0.6rem;
}
.section-label::after {
    content: "";
    flex: 1;
    height: 1px;
    background: rgba(255,255,255,0.1);
}

input[type="text"] {
    background: var(--ink-soft) !important;
    border: 1.5px solid rgba(255,255,255,0.12) !important;
    border-radius: 10px !important;
    color: var(--paper) !important;
}
input[type="text"]:focus {
    border-color: var(--amber) !important;
    box-shadow: 0 0 0 1px var(--amber) !important;
}

.match-pill {
    display: inline-block;
    background: rgba(232, 168, 73, 0.12);
    border: 1px solid var(--amber-dim);
    color: var(--amber);
    padding: 0.3rem 0.9rem;
    border-radius: 999px;
    font-family: 'Fraunces', serif;
    font-size: 1.05rem;
    margin-top: 0.5rem;
}
.no-match {
    color: var(--coral);
    font-size: 0.92rem;
    margin-top: 0.5rem;
}

.graph-node {
    display: inline-block;
    background: var(--ink-soft);
    border: 1px solid rgba(255,255,255,0.1);
    color: var(--slate);
    padding: 0.25rem 0.7rem;
    border-radius: 8px;
    font-size: 0.82rem;
    margin: 0.15rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------
st.markdown('<div class="eyebrow">Netra-AI · Navigation Core</div>', unsafe_allow_html=True)
st.markdown('<div class="headline">Say where you\'re going.</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subhead">This is the routing brain behind Netra-AI\'s voice assistant for '
    'campus navigation — without the camera, mic, or models. Tap the mic and say something like '
    '"main gate to lab complex," or pick the two points manually below.</div>',
    unsafe_allow_html=True,
)

# ---------------- Voice input (browser mic via Web Speech API) ----------------
# Runs entirely in the browser — no PyAudio/sounddevice install, works on
# Streamlit Cloud too. The transcript is sent back to Streamlit by setting
# a URL query param, which we read on the Python side below.
components.html(
    """
    <div style="font-family:'Inter',sans-serif;">
      <button id="mic-btn" style="
          background:#e8a849; color:#1a1f2e; border:none; border-radius:999px;
          padding:0.65rem 1.6rem; font-weight:600; font-size:0.95rem;
          cursor:pointer; display:flex; align-items:center; gap:0.5rem;">
        🎙 Tap to speak
      </button>
      <span id="mic-status" style="margin-left:0.7rem; color:#8891a3; font-size:0.88rem;"></span>
    </div>
    <script>
      const btn = document.getElementById('mic-btn');
      const status = document.getElementById('mic-status');
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

      if (!SpeechRecognition) {
        status.innerText = "Voice input isn't supported in this browser — try Chrome.";
        btn.disabled = true;
      } else {
        const recognition = new SpeechRecognition();
        recognition.lang = 'en-IN';
        recognition.interimResults = false;
        recognition.maxAlternatives = 1;

        btn.addEventListener('click', () => {
          status.innerText = "Listening...";
          recognition.start();
        });

        recognition.onresult = (event) => {
          const transcript = event.results[0][0].transcript;
          status.innerText = 'Heard: "' + transcript + '"';
          const url = new URL(window.parent.location);
          url.searchParams.set('voice_phrase', transcript);
          url.searchParams.set('ts', Date.now());
          window.parent.history.replaceState({}, '', url);
          window.parent.location.reload();
        };

        recognition.onerror = (event) => {
          status.innerText = "Didn't catch that — try again.";
        };
      }
    </script>
    """,
    height=60,
)

# Read the transcript the mic widget wrote into the URL query string.
heard_phrase = st.query_params.get("voice_phrase", "")

default_start = LOCATIONS.index("Main Gate")
default_dest = LOCATIONS.index("LC")

if heard_phrase:
    vs, vd = parse_start_destination(heard_phrase)
    if vs and vd:
        default_start = LOCATIONS.index(vs)
        default_dest = LOCATIONS.index(vd)
        st.markdown(
            f'<div class="match-pill">🎙 Heard "{heard_phrase}" → {vs} to {vd}</div>',
            unsafe_allow_html=True,
        )
    else:
        single = match_location(heard_phrase)
        if single:
            default_dest = LOCATIONS.index(single)
            st.markdown(
                f'<div class="match-pill">🎙 Heard "{heard_phrase}" → matched {single} '
                f'(set as destination — say "X to Y" to set both)</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'<div class="no-match">🎙 Heard "{heard_phrase}" but couldn\'t match a known location.</div>',
                unsafe_allow_html=True,
            )

# Map clicks (from the interactive campus map further down the page)
# also feed into the same defaults — read them before the dropdowns render.
map_start = st.query_params.get("map_start", "")
map_dest = st.query_params.get("map_dest", "")
next_pick = st.query_params.get("next_pick", "start")

if map_start and map_start in LOCATIONS:
    default_start = LOCATIONS.index(map_start)
if map_dest and map_dest in LOCATIONS:
    default_dest = LOCATIONS.index(map_dest)

# ---------------- Route builder ----------------
col1, col2, col3 = st.columns([1, 1, 0.001])
with col1:
    start = st.selectbox("From", LOCATIONS, index=default_start, label_visibility="collapsed")
with col2:
    destination = st.selectbox("To", LOCATIONS, index=default_dest, label_visibility="collapsed")

go = st.button("Walk this route →")

if go or heard_phrase:
    if start == destination:
        st.markdown(
            '<div class="route-summary">You\'re already there. Nowhere to walk.</div>',
            unsafe_allow_html=True,
        )
    else:
        path = find_path(campus_graph, start, destination)
        if not path:
            st.markdown(
                '<div class="no-match">No path connects these two points on the graph.</div>',
                unsafe_allow_html=True,
            )
        else:
            summary = get_route_summary(path)
            instructions = generate_instructions(path)

            st.markdown(f'<div class="route-summary">🔊 "{summary}"</div>', unsafe_allow_html=True)

            placeholder = st.empty()
            rendered = ""
            for i, step in enumerate(instructions, 1):
                frm, txt = step.split(":", 1)
                frm = frm.replace("From ", "").strip()
                rendered += (
                    f'<div class="step-card">'
                    f'<div class="step-num">{i:02d}</div>'
                    f'<div><span class="step-from">from {frm}</span>'
                    f'<span class="step-text">{txt.strip()}</span></div>'
                    f'</div>'
                )
                placeholder.markdown(rendered, unsafe_allow_html=True)
                time.sleep(0.18)

            st.success(f"Arrived at {destination}.")

# ---------------- Voice phrase tester ----------------
st.markdown('<div class="section-label">How it hears you</div>', unsafe_allow_html=True)
st.caption(
    "The real system listens for casual phrases, not exact names — "
    "\"canteen\" still resolves to Mayuri, typos and all."
)

phrase = st.text_input(
    " ",
    placeholder='Try: "canteen" or "main gate to lab complex"',
    label_visibility="collapsed",
)

if phrase:
    s, d = parse_start_destination(phrase)
    if s and d:
        st.markdown(
            f'<span class="match-pill">{s} → {d}</span>',
            unsafe_allow_html=True,
        )
    else:
        single = match_location(phrase)
        if single:
            st.markdown(f'<span class="match-pill">{single}</span>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="no-match">Didn\'t catch a known location in that.</div>', unsafe_allow_html=True)

# ---------------- Campus graph (interactive map) ----------------
st.markdown('<div class="section-label">The campus, as a map</div>', unsafe_allow_html=True)
st.caption("Click any building to set it as your start or destination — same graph as `campus_graph` in navigation.py.")

# Layout mirrors the real campus sketch: Main Gate sits between two
# branches — one running up through the hostels (GH1 → GH2 → AB2),
# the other running right through MPH → Mayuri, which forks again
# into AB1 and the UB → Architecture → LC corridor.
NODE_POS = {
    "Main Gate":     (130, 330),
    "GH1":           (130, 210),
    "GH2":           (130, 90),
    "AB2":           (290, 90),
    "MPH":           (300, 330),
    "Mayuri":        (470, 330),
    "AB1":           (470, 450),
    "UB":            (470, 210),
    "Architecture":  (620, 90),
    "LC":            (470, 90),
}

EDGES_DRAWN = set()
edge_lines = []
for node, neighbors in campus_graph.items():
    for nb in neighbors:
        key = tuple(sorted([node, nb]))
        if key in EDGES_DRAWN:
            continue
        EDGES_DRAWN.add(key)
        x1, y1 = NODE_POS[node]
        x2, y2 = NODE_POS[nb]
        edge_lines.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#4a5568" stroke-width="2.5" />')

node_circles = []
for name, (x, y) in NODE_POS.items():
    label = name if len(name) <= 4 else name[:2].upper()
    node_circles.append(f'''
      <g class="map-node" data-name="{name}" style="cursor:pointer;" transform="translate({x},{y})">
        <circle r="30" fill="#232a3d" stroke="#c8923f" stroke-width="2" class="node-circle" />
        <text text-anchor="middle" dy="5" fill="#e8a849" font-family="Fraunces, serif" font-size="15" font-weight="500" style="pointer-events:none;">{label}</text>
        <text text-anchor="middle" dy="46" fill="#8891a3" font-family="Inter, sans-serif" font-size="11" style="pointer-events:none;">{name}</text>
      </g>''')

svg_map = f'''
<svg viewBox="-20 0 720 500" style="width:100%; height:auto; font-family:Inter,sans-serif;">
  {"".join(edge_lines)}
  {"".join(node_circles)}
</svg>
'''

components.html(
    f"""
    <div style="background:#1a1f2e; border-radius:14px; padding:0.5rem 0;">
      {svg_map}
    </div>
    <style>
      .map-node:hover .node-circle {{ fill: #e8a849 !important; }}
      .map-node:hover text {{ fill: #1a1f2e !important; }}
    </style>
    <script>
      document.querySelectorAll('.map-node').forEach(function(el) {{
        el.addEventListener('click', function() {{
          const name = el.getAttribute('data-name');
          const url = new URL(window.parent.location);
          const role = url.searchParams.get('next_pick') === 'dest' ? 'map_dest' : 'map_start';
          url.searchParams.set(role, name);
          url.searchParams.set('next_pick', role === 'map_start' ? 'dest' : 'start');
          url.searchParams.set('ts', Date.now());
          window.parent.history.replaceState({{}}, '', url);
          window.parent.location.reload();
        }});
      }});
    </script>
    """,
    height=520,
)

if map_start or map_dest:
    pieces = []
    if map_start:
        pieces.append(f"start set to **{map_start}**")
    if map_dest:
        pieces.append(f"destination set to **{map_dest}**")
    next_label = "start" if next_pick == "start" else "destination"
    st.markdown(
        f'<div class="match-pill">{" · ".join(pieces)} — dropdowns above updated. Next click sets the {next_label}.</div>',
        unsafe_allow_html=True,
    )

st.markdown(
    '<div style="margin-top:3rem; color:var(--slate); font-size:0.82rem;">'
    'Built on Netra-AI\'s existing navigation.py and location_matcher.py — no routing logic duplicated.'
    '</div>',
    unsafe_allow_html=True,
)