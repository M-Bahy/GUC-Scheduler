import os
from PyPDF2 import PdfMerger


def combine_pdfs(folder_name, output_filename):
    pdf_merger = PdfMerger()

    def sort_key(file):
        # Extract the numeric part of the filename for sorting
        return int("".join(filter(str.isdigit, file)) or 0)

    for root, _, files in os.walk(folder_name):
        for file in sorted(files, key=sort_key):
            if file.endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                pdf_merger.append(pdf_path)

    pdf_merger.write(output_filename)
    pdf_merger.close()
