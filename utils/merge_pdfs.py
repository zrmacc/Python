# Usage: python merge_pdfs.py pdf1.pdf pdf2.pdf pdf3.pdf

from typing import List

import os
import PyPDF2
import sys


def merge_pdfs(files: List[str], output_name="merged.pdf") -> None:
	"""Merge list of PDFs."""
	merger = PyPDF2.PdfFileMerger()
	for file in files:
		if os.path.exists(file):
			merger.append(file)
		else:
			print(f"{file} does not exist.")

	if len(merger.pages) > 0:
		merger.write(output_name)
		print(f"Merged document written to: {output_name}")
	else:
		print("No documents to merge.")

	merger.close()


if __name__ == "__main__":
	files = sys.argv[1:]
	merge_pdfs(files)
