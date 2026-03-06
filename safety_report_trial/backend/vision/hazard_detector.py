try:
    from ultralytics import YOLO
except ImportError:
    YOLO = None

model = YOLO("yolov8n.pt") if YOLO else None

def detect_ppe(image_path):
    if model is None:
        return {"message": "Vision module disabled"}

    results = model(image_path)

    detections = []
    for r in results:
        for box in r.boxes:
            detections.append({
                "class": int(box.cls[0]),
                "confidence": float(box.conf[0])
            })

    return detections