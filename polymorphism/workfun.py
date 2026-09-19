class Developer:
    def work(self):
        print("Developer works")
class Tester:
    def work(self):
        print("Tester works")
class Manager:
    def work(self):
        print("Manager works")
def work(x):
    x.work()
d=Developer()
t=Tester()
m=Manager()
work(d)
work(t)
work(m)