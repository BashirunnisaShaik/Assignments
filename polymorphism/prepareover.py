class Food:
    def pre(self):
        print("Preparing food")
class Pizza(Food):
    def pre(self):
        print("Preparing Pizza")
class Burger(Food):
    def pre(self):
        print("Preparing Burger")
class Biryani(Food):
    def pre(self):
        print("Preparing Biryani")
Pizza().pre()
Burger().pre()
Biryani().pre()