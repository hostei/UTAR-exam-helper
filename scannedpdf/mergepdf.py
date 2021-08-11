from PyPDF2 import PdfFileMerger
import webbrowser
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

def list_files(directory, extension):
    return (f for f in os.listdir(directory) if f.endswith('.' + extension))

pdfs = list_files(dir_path, "pdf")

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

with open('UCCM1153_Quiz_CS_21ACB0xxxx.pdf', 'wb') as fout:
    merger.write(fout)

webbrowser.open_new('file://'+ dir_path + '/UCCM1153_Quiz_CS_21ACB0xxxx.pdf')
