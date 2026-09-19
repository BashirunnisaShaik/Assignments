class TextFile:
    def read(self):
        print("Reading text file")
class PDFFile:
    def read(self):
        print("Reading PDF file")
class WordFile:
    def read(self):
        print("Reading Word file")
def read(x):
    x.read()
t=TextFile()
p=PDFFile()
w=WordFile()
read(t)
read(p)
read(w)