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
            print("\nProcessing PDF files:")
            for pdf_file in pdf_files:
                pdf_path = os.path.join(folder_path, pdf_file)
                pdf_text = extract_text_from_pdf(pdf_path)
                if pdf_text:
                    print(f"\nText extracted from {pdf_file}:")
                    print(pdf_text)
                else:
                    print(f"\nUnsupported format or error occurred while extracting text from {pdf_file}.")
        else:
            print("\nNo PDF files found.")

        if 'docx' in file_types:
            docx_files = file_types['docx']
            print("\nProcessing DOCX files:")
            for docx_file in docx_files:
                docx_path = os.path.join(folder_path, docx_file)
                docx_text = extract_text_from_docx(docx_path)
                if docx_text:
                    print(f"\nText extracted from {docx_file}:")
                    print(docx_text)
                else:
                    print(f"\nUnsupported format or error occurred while extracting text from {docx_file}.")
        else:
            print("\nNo DOCX files found.")

        if 'img' in file_types:
            myconfig = "--psm 11 --oem 3"
            img_files = file_types['img']
            print("\nProcessing image files:")
            for img_file in img_files:
                img_path = os.path.join(folder_path, img_file)
                img_text = extract_text_from_image(img_path, config=myconfig)
                if img_text:
                    print(f"\nText extracted from {img_file}:")
                    print(img_text)
                else:
                    print(f"\nError occurred while extracting text from {img_file}.")
        else:
            print("\nNo image files found.")
    else:
        print("No files found in the specified folder.")

except Exception as e:
    print(f"An error occurred: {e}")















