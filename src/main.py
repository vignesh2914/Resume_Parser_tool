import os
from scraper import extract_text_from_pdf, extract_text_from_docx, extract_text_from_image, file_format_verification

try:
    folder_path = "dataset"
    file_types = file_format_verification(folder_path)
    
    if file_types:
        print("Found the following files:")
        for file_type, files in file_types.items():
            print(f"{file_type.upper()} files: {', '.join(files)}")

        if 'pdf' in file_types:
            pdf_files = file_types['pdf']
            print("Processing PDF files:")
            for pdf_file in pdf_files:
                pdf_path = os.path.join(folder_path, pdf_file)
                try:
                    pdf_text = extract_text_from_pdf(pdf_path)
                    if pdf_text:
                        print(f"Text extracted from {pdf_file}: {pdf_text}")
                    else:
                        print(f"Unsupported format or error occurred while extracting text from {pdf_file}.")
                except Exception as e:
                    print(f"Error processing PDF file {pdf_file}: {e}")
        else:
            print("No PDF files found.")

        if 'docx' in file_types:
            docx_files = file_types['docx']
            print("Processing DOCX files:")
            for docx_file in docx_files:
                docx_path = os.path.join(folder_path, docx_file)
                try:
                    docx_text = extract_text_from_docx(docx_path)
                    if docx_text:
                        print(f"Text extracted from {docx_file}: {docx_text}")
                    else:
                        print(f"Unsupported format or error occurred while extracting text from {docx_file}.")
                except Exception as e:
                    print(f"Error processing DOCX file {docx_file}: {e}")
        else:
            print("No DOCX files found.")

        if 'img' in file_types:
            myconfig = "--psm 11 --oem 3"
            img_files = file_types['img']
            print("Processing image files:")
            for img_file in img_files:
                img_path = os.path.join(folder_path, img_file)
                try:
                    img_text = extract_text_from_image(img_path, config=myconfig)
                    if img_text:
                        print(f"Text extracted from {img_file}: {img_text}")
                    else:
                        print(f"Error occurred while extracting text from {img_file}.")
                except Exception as e:
                    print(f"Error processing image file {img_file}: {e}")
        else:
            print("No image files found.")
    else:
        print("No files found in the specified folder.")

except Exception as e:
    print(f"An error occurred: {e}")
