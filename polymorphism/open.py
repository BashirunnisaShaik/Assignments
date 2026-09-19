class PDF:
    def open(self):
        print("Opening PDF")
class Word:
    def open(self):
        print("Opening Word")
class Excel:
    def open(self):
        print("Opening Excel")
p=PDF()
w=Word()
e=Excel()
p.open()
w.open()
e.open()