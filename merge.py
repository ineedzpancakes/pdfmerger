# first, have python 3 installed
# second, install the PyPDF2 module by typing "pip install PyPDF2" in your terminal

# do the following imports
import os
from PyPDF2 import PdfFileMerger

# make sure the python file (this code) and all your pdfs are in the same folder when you run the code
source = os.getcwd()

# from here on, the merge process begins
# if you want to merge pdfs in a particular order, that's up to you to figure it out (it's not hard)
for item in os.listdir(source):
  if item.endswith("pdf):
    merge.append(item)
merge.write("Merged.pdf")
merge.close()
