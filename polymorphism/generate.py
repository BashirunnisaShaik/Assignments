class ExcelReport:
    def generate(self):
        print("Excel report")
class PDFReport:
    def generate(self):
        print("PDF report")
def report(x):
    x.generate()
e=ExcelReport()
p=PDFReport()
report(e)
report(p)