import requests
import os

DOWNLOAD_FOLDER = "dataset_builder/pdfs"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def download_pdf(url):
	filename = url.split("/")[-1]
	filepath = os.path.join(DOWNLOAD_FOLDER, filename)
	response = requests.get(url)
	if response.status_code == 200:
		with open(filepath, "wb") as f:
			f.write(response.content)
		print(f"Downloaded: {filename}")
		return filepath
	print("Failed to download:", url)
	return None
# pdf_downloader.py
# PDF downloading logic