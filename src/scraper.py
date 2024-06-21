import logging
import os
from docx import Document
import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import io


def file_format_verification(folder_path):
    logging.info("Starting file format verification")
    
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            logging.debug(f"Created directory: {folder_path}")

        file_types = {
            'pdf': [],
            'img': [],
            'docx': [],
            'other': []
        }

        for file in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, file)):
                _, extension = os.path.splitext(file)
                extension = extension[1:].lower() 

                if extension == 'pdf':
                    file_types['pdf'].append(file)
                elif extension in ['jpg', 'jpeg', 'png', 'gif']:
                    file_types['img'].append(file)
                elif extension == 'docx':
                    file_types['docx'].append(file)
                else:
                    file_types['other'].append(file)

        for file_type, files in file_types.items():
            if files:
                logging.info(f"Found {len(files)} {file_type.upper()} file(s): {files}")

        return file_types
    
    except Exception as e:
        logging.error(f"Error during file format verification: {e}")
        return None

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            images = page.get_images()
            if images:
                for img_index, img_info in enumerate(images):
                    xref = img_info[0]
                    base_image = doc.extract_image(xref)
                    image_bytes = base_image["image"]
                    image = Image.open(io.BytesIO(image_bytes))
                    text += pytesseract.image_to_string(image)
            elif not images:  
                text += page.get_text()
            else:  
                logging.warning(f"Unsupported format in PDF: {pdf_path}")
                return None
        logging.info(f"Text extracted from PDF: {pdf_path}")
        return text.strip()
    except Exception as e:
        logging.error(f"Error extracting text from PDF: {e}")
        return None

def extract_text_from_docx(file_path):
    try:
        doc = Document(file_path)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        logging.info(f"Text extracted from DOCX: {file_path}")
        return text
    except Exception as e:
        logging.error(f"Error extracting text from DOCX: {e}")
        return None



















































