import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


args = sys.argv
input_path = args[1] # pdf file
output_path = args[2] # txt file

manager = PDFResourceManager()

with open(output_path, "wb") as output:
    with open(input_path, 'rb') as input:
        with TextConverter(manager, output, codec='utf-8', laparams=LAParams()) as conv:
            interpreter = PDFPageInterpreter(manager, conv)
            for page in PDFPage.get_pages(input):
                interpreter.process_page(page)