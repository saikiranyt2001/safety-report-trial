# website_scraper.py
# Website scraping logic

import pdfplumber
import requests
from bs4 import BeautifulSoup

def read_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def get_pdf_links(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to load page")
        return []
    soup = BeautifulSoup(response.text, "html.parser")
    pdf_links = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if href and href.endswith(".pdf"):
            pdf_links.append(href)
    return pdf_links