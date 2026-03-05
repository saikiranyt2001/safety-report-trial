from docx import Document

def fill_template(data):
	doc = Document("template.docx")
	for paragraph in doc.paragraphs:
		for key, value in data.items():
			if f"{{{{{key}}}}}" in paragraph.text:
				paragraph.text = paragraph.text.replace(f"{{{{{key}}}}}", value)
	output_file = "generated_report.docx"
	doc.save(output_file)
	return output_file