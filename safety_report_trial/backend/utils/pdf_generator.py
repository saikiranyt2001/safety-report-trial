# PDF Generator Utility
from fpdf import FPDF

def generate_pdf(report_text, filename="safety_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in report_text.split("\n"):
        pdf.cell(200, 10, txt=line, ln=True)
    pdf.output(filename)
