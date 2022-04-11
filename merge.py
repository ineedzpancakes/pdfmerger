import os
from PyPDF2 import PdfFileMerger
source = os.getcwd()

for item in os.listdir(source):
  if item.endswith("pdf):
    merge.append(item)
merge.write("Merged.pdf")
merge.close()
