from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def export_pdf(content):
	file_path = "safety_report.pdf"
	c = canvas.Canvas(file_path, pagesize=letter)
	textobject = c.beginText(40, 750)
	for line in content.split("\n"):
		textobject.textLine(line)
	c.drawText(textobject)
	c.save()
	return file_path