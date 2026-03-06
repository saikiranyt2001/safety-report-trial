# Hazard Image Detection (YOLOv8 Example)
from ultralytics import YOLO

def detect_ppe(image_path):
    model = YOLO("yolov8n.pt")
    results = model(image_path)
    return results
