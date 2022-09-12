"""
Split PDF File

"""

__author__ = "Hephzibah Pon Cellat Arulprakash"
__credits__ = ["Hephzibah Pon Cellat Arulprakash"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Hephzibah Pon Cellat Arulprakash"
__email__ = "poncellat@gmail.com"
__status__ = "Production"


from PyPDF2 import PdfFileWriter, PdfFileReader
import sys


def split_pdf():
    filename = sys.argv[1]
    start_page = sys.argv[2]
    end_page = sys.argv[3]

    inputpdf = PdfFileReader(open(filename, "rb"))

    output = PdfFileWriter()
    for i in range(int(start_page), int(end_page)+1):
        output.addPage(inputpdf.getPage(i))

    with open('-'.join([filename[:-4], start_page, end_page + ".pdf"]), "wb") as fp:
        output.write(fp)
        print("done")





if __name__ == "__main__":
    split_pdf()
