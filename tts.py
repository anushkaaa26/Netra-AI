# tts.py
import subprocess

def speak(text):
    print(f"🔊 {text}")
    try:
        subprocess.run(["say", "-r", "160", text], check=True)
    except Exception as e:
        print(f"❌ TTS error: {e}")