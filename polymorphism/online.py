class OnlineCourse:
    def start(self):
        print("Online course")
class OfflineCourse:
    def start(self):
        print("Offline course")
def start(x):
    x.start()
o=OnlineCourse()
f=OfflineCourse()
start(o)
start(f)