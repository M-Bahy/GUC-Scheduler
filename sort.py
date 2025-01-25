import os
import shutil
import re


def distribute_pdfs(directory):
    # Define the subfolder names and their corresponding regex patterns
    subfolders = {
        "NETW1009_L001_DMET1067_L001": re.compile(
            r"^NETW1009_L001_.*_DMET1067_L001_.*\.pdf$"
        ),
        "NETW1009_L002_DMET1067_L001": re.compile(
            r"^NETW1009_L002_.*_DMET1067_L001_.*\.pdf$"
        ),
    }

    # Create the subfolders if they do not exist
    for subfolder in subfolders.keys():
        subfolder_path = os.path.join(directory, subfolder)
        os.makedirs(subfolder_path, exist_ok=True)

    # Get a list of all PDF files in the directory
    pdf_files = [f for f in os.listdir(directory) if f.endswith(".pdf")]

    # Distribute the PDFs into the appropriate subfolders
    for pdf in pdf_files:
        for subfolder, pattern in subfolders.items():
            if pattern.match(pdf):
                src_path = os.path.join(directory, pdf)
                dest_path = os.path.join(directory, subfolder, pdf)
                shutil.move(src_path, dest_path)
                break


# Example usage:
distribute_pdfs("others/Bahy og PDFs")
print("Done")
