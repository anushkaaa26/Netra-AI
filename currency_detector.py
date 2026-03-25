import cv2
from ultralytics import YOLO
from tts import speak
import time

model = YOLO("models/currency.pt")

last_spoken = 0
cooldown = 3

def detect_currency():
    global last_spoken

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        speak("Camera error")
        return

    speak("Currency detection started")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, conf=0.6)

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                label = model.names[cls]

                current_time = time.time()

                if current_time - last_spoken > cooldown:
                    speak(f"{label} rupees detected")
                    last_spoken = current_time

        cv2.imshow("Currency Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('x'):
            break

    cap.release()
    cv2.destroyAllWindows()