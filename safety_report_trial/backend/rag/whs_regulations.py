# WHS Regulation Mapping for Australian Safety
REGULATION_MAP = {
    "working at height": "WHS Regulation Part 4.4 – Falls",
    "hazardous chemicals": "WHS Regulation Part 7.1",
    "electrical hazard": "WHS Regulation Part 4.7"
}

def get_regulation(hazard):
    return REGULATION_MAP.get(hazard, "General WHS Regulation")
