# money_detection.py
import cv2
from ultralytics import YOLO

model = YOLO("models/currency.pt")
cap = cv2.VideoCapture(0)

def detect_currency_frame():
    """Detects currency in a single frame. Returns list of labels or None."""
    if not cap.isOpened():
        return None

    ret, frame = cap.read()
    if not ret:
        return None

    results = model(frame, conf=0.6)

    detected = []
    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            detected.append(label)

    return detected if detected else None

def release_camera():
    """Call this when the app exits."""
    cap.release()
    cv2.destroyAllWindows()
