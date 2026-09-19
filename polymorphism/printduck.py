class Printer:
    def print(self):
        print("Printing")
class PDFPrinter:
    def print(self):
        print("Printing PDF")
def print_doc(x):
    x.print()
p=Printer()
pdf=PDFPrinter()
print_doc(p)
print_doc(pdf)