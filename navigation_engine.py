# navigation_engine.py
from navigation import start_navigation
from obstacle_navigation import detect_obstacle
from fall_detection import detect_fall
from text_reader import detect_text
from money_detection import detect_currency_frame, release_camera
from tts import speak
import time
import logging

last_spoken = 0
cooldown = 3

def _wait_with_detection(seconds=8):
    """Check for obstacles, falls, currency and text while user is walking."""
    global last_spoken
    end_time = time.time() + seconds
    last_obstacle_check = 0
    OBSTACLE_INTERVAL = 1.0

    while time.time() < end_time:
        current_time = time.time()

        # 🚨 FALL DETECTION
        if detect_fall():
            speak("Fall detected. Stopping navigation.")
            return "fall"

        # ⚠️ OBSTACLE DETECTION
        if current_time - last_obstacle_check > OBSTACLE_INTERVAL:
            last_obstacle_check = current_time
            direction = detect_obstacle()
            if direction and current_time - last_spoken > cooldown:
                if direction == "left":
                    speak("Obstacle on left, move right")
                elif direction == "right":
                    speak("Obstacle on right, move left")
                else:
                    speak("Obstacle ahead, stop")
                last_spoken = current_time
                time.sleep(0.5)
                continue

        # 💵 CURRENCY DETECTION
        labels = detect_currency_frame()
        if labels and current_time - last_spoken > cooldown:
            for label in labels:
                speak(f"{label} rupees detected")
            last_spoken = current_time
            time.sleep(0.5)
            continue

        # 📖 TEXT DETECTION
        text = detect_text()
        if text and current_time - last_spoken > cooldown:
            speak(f"Text detected: {text}")
            last_spoken = current_time
            time.sleep(0.5)
            continue

        time.sleep(0.1)

    return "ok"


def run_navigation(start, destination):
    global last_spoken

    logging.getLogger("ultralytics").setLevel(logging.WARNING)

    instructions, summary = start_navigation(start, destination)

    if not instructions or instructions[0] == "No path found between these locations":
        speak("Sorry, no path found.")
        return

    # Speak full route summary first
    speak(summary)
    time.sleep(1)
    speak("I will now guide you step by step.")
    time.sleep(0.5)

    try:
        for i, instruction in enumerate(instructions):
            # 🧭 Speak current step
            speak(instruction)
            print(f"📍 Step {i + 1}/{len(instructions)}: {instruction}")
            last_spoken = time.time()

            # ✅ Walk window with live detection
            result = _wait_with_detection(seconds=8)
            if result == "fall":
                return  # stop everything on fall

        speak("You have arrived at your destination. Navigation complete.")

    finally:
        release_camera()