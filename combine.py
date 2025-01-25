import os
import shutil
from PyPDF2 import PdfMerger


def combine_pdfs(folder_path):
    def sort_key(file):
        # Extract the numeric part of the filename for sorting
        return int("".join(filter(str.isdigit, file)) or 0)

    for subfolder in os.listdir(folder_path):
        subfolder_path = os.path.join(folder_path, subfolder)
        if os.path.isdir(subfolder_path):
            pdf_merger = PdfMerger()
            for root, _, files in os.walk(subfolder_path):
                for file in sorted(files, key=sort_key):
                    if file.endswith(".pdf"):
                        pdf_path = os.path.join(root, file)
                        pdf_merger.append(pdf_path)

            combined_pdf_path = os.path.join(folder_path, f"{subfolder}.pdf")
            pdf_merger.write(combined_pdf_path)
            pdf_merger.close()

            # Delete the subfolder and its contents
            shutil.rmtree(subfolder_path)


# Example usage:
combine_pdfs("others/Bahy og PDFs")
print("Done")
