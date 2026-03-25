import random
import time
from tts import speak

def detect_fall():
    speak("Fall detection active")

    time.sleep(2)

    # Demo logic (placeholder)
    if random.choice([True, False]):
        speak("Warning! Fall detected")
    else:
        speak("No fall detected")