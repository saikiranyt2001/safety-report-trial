# Hazard Image Detection (YOLOv8 Example)
try:
    from ultralytics import YOLO
except ImportError:
    YOLO = None

def detect_ppe(image_path):
    if YOLO is None:
        return "Vision module disabled"
    model = YOLO("yolov8n.pt")
    results = model(image_path)
    return results
