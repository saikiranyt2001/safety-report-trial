# Report Agent for Structured Safety Reports

def generate_structured_report(site_data, hazards, risks, controls, compliance):
    report = f"""
INDUSTRIAL SAFETY REPORT\n------------------------------\n
Company: {site_data.get('company')}\nLocation: {site_data.get('location')}\nInspection Date: {site_data.get('inspection_date')}\n
Hazards Identified\n-------------------\n" + "\n".join([f"• {h}" for h in hazards]) + "\n\nRisk Assessment\n----------------\n" + "\n".join([f"{h} → {risks[h]}" for h in hazards]) + "\n\nControl Measures\n----------------\n" + "\n".join([str(controls[h]) for h in hazards]) + "\n\nCompliance\n-----------\n" + "\n".join(compliance) + "\n\nRecommendations\n---------------\n" + site_data.get('recommendations', '') + "\n\nReview Date\n------------\n" + site_data.get('review_date', '') + "\n"
    return report
