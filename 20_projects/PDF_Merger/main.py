# merge PDF files. This project involves combining multiple PDF documents into one, allowing you to automate file handling, improve productivity, and streamline document management.
from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []
n = int(input("How many pdfs do you want to merge?\n"))
# This is a nice way to iterate using for loops in Python 
# This is nice but throws
for i in range(0, n): 
    name = input(f"Enter the name of pdf {i + 1}: ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()