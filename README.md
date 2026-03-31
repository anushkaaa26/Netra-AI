# 👁️ Netra-AI

**Real-time assistive navigation system for the visually impaired**

> *Netra* (Sanskrit) = Eye — AI for sight beyond vision

Netra-AI is an open-source, voice-interactive navigation system built for visually impaired individuals. It combines campus navigation, real-time obstacle detection, fall detection, currency recognition, and text reading into a single hands-free pipeline — all communicated through voice.



---

## 🎯 What It Does

| Module | What happens |
|---|---|
| 🎙️ **Voice Navigation** | User speaks start & destination → system plans route → speaks turn-by-turn directions |
| ⚠️ **Obstacle Detection** | YOLOv8 detects objects in camera feed → alerts "obstacle on left, move right" etc. |
| 🚨 **Fall Detection** | Detects user falls → immediately stops navigation and announces alert |
| 💵 **Currency Recognition** | Custom YOLO model identifies Indian rupee denominations in real time |
| 📖 **Text Reader** | Tesseract OCR reads signboards and printed text aloud |
| 🔊 **Voice Output** | All output delivered via text-to-speech — no screen needed |

---

## 🗺️ Campus Navigation (VIT Bhopal)

The system uses a handcrafted campus graph with physically accurate turn-by-turn directions based on real observation of the VIT Bhopal layout.

```
Main Gate ──── GH1 ──── GH2 ──── AB2
    │
   MPH ──── Mayuri ──── UB ──── Architecture ──── Lab Complex
                │
               AB1
```

**Example route — Main Gate → Lab Complex:**
1. Go a little straight, then turn right towards MPH
2. Go straight, then turn left, then turn right towards Mayuri
3. Take the next right towards UB
4. Turn right and go straight. Architecture block is on your right side
5. Go straight ahead. Lab Complex will be on your left side

---

## 🏗️ Architecture

```
User speaks
    │
    ▼
Voice Input (sounddevice + Google STT)
    │
    ▼
Location Matcher (alias → fuzzy matching)
    │
    ▼
Navigation Module (BFS pathfinding + DIRECTIONS map)
    │
    ▼
Navigation Engine ◄─── orchestrates everything
    │
    ├── Obstacle Detection  (YOLOv8, every 1s)
    ├── Fall Detection      (every tick — highest priority)
    ├── Currency Detection  (custom YOLO model)
    └── Text Reader         (Tesseract OCR)
    │
    ▼
TTS Output (macOS say / pyttsx3)
    │
    ▼
User hears
```

---

## 📁 Project Structure

```
NetraAI/
├── main.py                  # Entry point — runs the full system
├── navigation_engine.py     # Core orchestrator + walking window loop
├── navigation.py            # Campus graph, BFS pathfinding, directions
├── location_matcher.py      # Voice → canonical location name
├── voice_input.py           # Microphone capture + Google STT
├── tts.py                   # Text-to-speech output
├── obstacle_navigation.py   # YOLOv8 obstacle detection
├── fall_detection.py        # Camera-based fall detection
├── money_detection.py       # Indian currency recognition
├── text_reader.py           # Tesseract OCR text reading
└── models/
    └── currency.pt          # Custom-trained YOLO currency model
```

---

## ⚙️ Installation

### Prerequisites
- Python 3.10+
- macOS (for `say` TTS command) — or swap `tts.py` for pyttsx3 on other OS
- Webcam / USB camera
- Microphone

### Setup

```bash
# Clone the repo
git clone https://github.com/yourusername/NetraAI.git
cd NetraAI

# Install dependencies
pip install ultralytics opencv-python sounddevice scipy \
            SpeechRecognition pytesseract pillow numpy
```

### Tesseract OCR

```bash
# macOS
brew install tesseract

# Ubuntu / Debian
sudo apt install tesseract-ocr
```

### Place your model

Put your trained currency model inside the `models/` folder:
```
models/currency.pt
```

---

## 🚀 Run

```bash
python main.py
```

The system will:
1. Greet the user by voice
2. Ask for current location and destination
3. Speak the full route summary
4. Guide step by step with live obstacle and fall detection

**Example voice interaction:**
```
System : "Please say your start and destination."
User   : "main gate to lab complex"
System : "Got it. Main Gate to Lab Complex."
System : "Say yes to start or no to cancel."
User   : "yes"
System : "Your route has 5 steps. You will pass through:
          Main Gate, MPH, Mayuri, UB, Architecture, Lab Complex."
System : "From Main Gate: Go a little straight, then turn right towards MPH."
         [walking... obstacle detection running...]
System : "Obstacle on left, move right."
         [continues walking...]
System : "From MPH: Go straight, then turn left, then turn right towards Mayuri."
...
System : "You have arrived at your destination. Navigation complete."
```

---

## 🧠 How Voice Matching Works

Users don't have to say exact location names. Netra-AI uses a 3-tier matching system:

| Tier | Method | Example |
|---|---|---|
| 1 | Alias map | "canteen" → Mayuri |
| 2 | Substring match | "hostel 1" → GH1 |
| 3 | Fuzzy match (difflib) | "architectur" → Architecture |

Combined phrases also work:
```
"main gate to lab"  →  start: Main Gate, destination: Lab Complex
```

---

## 📊 Performance

| Module | Accuracy | Notes |
|---|---|---|
| Voice Input (STT) | ~88% | Reduces in noisy outdoor environments |
| Location Matching | ~95% | Handles informal and mispronounced names |
| Navigation (BFS) | 100% | Deterministic on static graph |
| Obstacle Detection | ~90% | YOLOv8, conf=0.6, 50–90ms/frame |
| Currency Detection | ~87% | Custom model, all major rupee denominations |
| Text Detection (OCR) | ~82% | Depends on lighting and camera stability |
| Fall Detection | ~85% | Camera-based, works under normal lighting |
| TTS Output | 100% | Synchronous, never fails |

---

## 🔧 Configuration

Tune these values in `navigation_engine.py`:

```python
cooldown = 3              # seconds between TTS announcements
OBSTACLE_CHECK_INTERVAL = 1.0   # how often to check for obstacles (seconds)
seconds = 8               # walking window duration per step
```

Adjust walking window per location in `navigation_engine.py`:
```python
STEP_DURATIONS = {
    "Main Gate": 10,
    "MPH": 8,
    "Mayuri": 6,
    ...
}
```

---

## 🗣️ Adding New Campus Locations

1. Add the node to `campus_graph` in `navigation.py`:
```python
campus_graph = {
    ...
    "New Building": ["Mayuri", "UB"],
}
```

2. Add directional instructions to `DIRECTIONS`:
```python
DIRECTIONS = {
    ...
    ("Mayuri", "New Building"): "Turn left and go straight. New Building is ahead.",
    ("New Building", "Mayuri"): "Turn around and go straight back to Mayuri.",
}
```

3. Add spoken aliases to `ALIASES` in `location_matcher.py`:
```python
ALIASES = {
    ...
    "new building": "New Building",
    "nb": "New Building",
}
```

---

## 🔮 Future Work

- [ ] GPS integration for hybrid indoor/outdoor navigation
- [ ] Wearable form factor (smart glasses / chest-mounted camera)
- [ ] Offline speech recognition (Vosk) for no-internet operation
- [ ] Expand campus graph to full VIT Bhopal campus
- [ ] Android/iOS companion app
- [ ] Multi-language TTS support (Hindi, regional languages)

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) — object detection
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) — text reading
- [OpenCV](https://opencv.org) — camera and image processing
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) — Google STT wrapper
- VIT Bhopal University EPICS Program

---

<p align="center">Built with ❤️ for the visually impaired community — VIT Bhopal University, 2025</p>
