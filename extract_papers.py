#!/usr/bin/env python3
"""
Extract text and images from PDF files in the paper/ directory.
Saves text to extracted/text/ and images to extracted/images/.
"""

import os
import fitz  # PyMuPDF
from PIL import Image
import io
import re

def sanitize_filename(name):
    """Sanitize filename to be safe for filesystem."""
    return re.sub(r'[^\w\-_\.]', '_', name)

def extract_pdfs():
    paper_dir = 'paper'
    text_dir = 'extracted/text'
    image_dir = 'extracted/images'

    if not os.path.exists(text_dir):
        os.makedirs(text_dir)
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    pdf_files = [f for f in os.listdir(paper_dir) if f.lower().endswith('.pdf')]
    total_pdfs = len(pdf_files)

    for idx, pdf_file in enumerate(pdf_files, 1):
        pdf_path = os.path.join(paper_dir, pdf_file)
        base_name = sanitize_filename(os.path.splitext(pdf_file)[0])

        print(f"Processing PDF {idx}/{total_pdfs}: {pdf_file}")

        try:
            doc = fitz.open(pdf_path)
            total_pages = len(doc)

            for page_num in range(total_pages):
                page = doc.load_page(page_num)
                page_num_str = f"{page_num + 1:02d}"

                # Extract text
                text = page.get_text()
                text_filename = f"{base_name}_page_{page_num_str}.txt"
                text_path = os.path.join(text_dir, text_filename)
                with open(text_path, 'w', encoding='utf-8') as f:
                    f.write(text)

                # Extract image (render to PNG)
                pix = page.get_pixmap(dpi=150)  # Adjust DPI as needed
                img_data = pix.tobytes("png")
                img = Image.open(io.BytesIO(img_data))
                img_filename = f"{base_name}_page_{page_num_str}.png"
                img_path = os.path.join(image_dir, img_filename)
                img.save(img_path)

                print(f"  Extracted page {page_num + 1}/{total_pages}")

            doc.close()
        except Exception as e:
            print(f"Error processing {pdf_file}: {e}")

    print("PDF extraction completed.")

if __name__ == "__main__":
    extract_pdfs()