class PDF:
    def generate(self):
        print("PDF report generated")
class Excel:
    def generate(self):
        print("Excel report generated")
class Word:
    def generate(self):
        print("Word report generated")
def generate(x):
    x.generate()
p=PDF()
e=Excel()
w=Word()
generate(p)
generate(e)
generate(w)