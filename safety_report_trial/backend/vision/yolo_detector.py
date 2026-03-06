# yolo_detector.py
"""
Hazard Image Detection Module
Supports PPE, helmet, and safety vest detection using YOLOv8 or similar models.
"""


from ultralytics import YOLO

class HazardDetector:
    def __init__(self, model_path=None):
        self.model_path = model_path or "yolov8n.pt"  # Default to YOLOv8 nano
        self.model = YOLO(self.model_path)

    def detect_ppe(self, image_path):
        results = self.model(image_path)
        ppe_labels = ["ppe", "gloves", "boots", "goggles"]
        detected = [r for r in results[0].boxes.data if r[-1] in ppe_labels]
        return {
            "ppe_detected": bool(detected),
            "details": f"Detected PPE: {len(detected)} items"
        }

    def detect_helmet(self, image_path):
        results = self.model(image_path)
        helmet_labels = ["helmet", "hardhat"]
        detected = [r for r in results[0].boxes.data if r[-1] in helmet_labels]
        return {
            "helmet_detected": bool(detected),
            "details": f"Detected Helmets: {len(detected)} items"
        }

    def detect_safety_vest(self, image_path):
        results = self.model(image_path)
        vest_labels = ["vest", "safety vest"]
        detected = [r for r in results[0].boxes.data if r[-1] in vest_labels]
        return {
            "vest_detected": bool(detected),
            "details": f"Detected Vests: {len(detected)} items"
        }

# Example usage:
# detector = HazardDetector(model_path="yolov8n.pt")
# result = detector.detect_ppe("image.jpg")
