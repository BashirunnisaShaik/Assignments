class Computer:
    def process(self):
        print("Computer processing")
class Laptop(Computer):
    def process(self):
        print("Laptop processing")
class Desktop(Computer):
    def process(self):
        print("Desktop processing")
class Server(Computer):
    def process(self):
        print("Server processing")
Laptop().process()
Desktop().process()
Server().process()