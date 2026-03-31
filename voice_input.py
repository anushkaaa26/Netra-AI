# voice_input.py
import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import numpy as np
import os
import time

def get_default_input_device():
    """Find a working input device index."""
    devices = sd.query_devices()
    for i, device in enumerate(devices):
        if device['max_input_channels'] > 0:
            print(f"🎤 Using mic: {device['name']} (index {i})")
            return i
    return None

def get_voice_command(prompt=None):
    from tts import speak
    if prompt:
        speak(prompt)
        time.sleep(0.6)   # wait for TTS to finish before opening mic

    fs = 16000
    duration = 5
    print("🎙️ Listening...")

    device_index = get_default_input_device()
    if device_index is None:
        print("❌ No input device found")
        return None

    try:
        recording = sd.rec(
            int(duration * fs),
            samplerate=fs,
            channels=1,
            dtype='int16',
            device=device_index   # ✅ explicitly set device
        )
        sd.wait()
    except Exception as e:
        print(f"❌ Mic error: {e}")
        return None

    write("temp.wav", fs, recording)

    r = sr.Recognizer()
    r.energy_threshold = 300
    r.pause_threshold = 0.8

    with sr.AudioFile("temp.wav") as source:
        audio = r.record(source)
        try:
            text = r.recognize_google(audio)
            print(f"✅ You said: {text}")
            return text.lower().strip()
        except sr.UnknownValueError:
            print("❌ Could not understand")
            return None
        except sr.RequestError:
            print("❌ Google STT unavailable")
            return None
        finally:
            if os.path.exists("temp.wav"):
                os.remove("temp.wav")