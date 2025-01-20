import os

def sort_pdfs(directory, n):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    # Get a list of all PDF files in the directory
    pdf_files = [f for f in os.listdir(directory) if f.endswith(".pdf")]

    # Check if any PDF files were found
    if not pdf_files:
        print(f"No PDF files found in directory '{directory}'.")
        return

    # Sort the PDF files by name
    sorted_pdfs = sorted(pdf_files)

    # Print the names of the first n items, each on a separate line
    for pdf in sorted_pdfs[:n]:
        print(pdf)

# Example usage:
sort_pdfs("others/Fahim og PDFs", 13)