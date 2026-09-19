class AndroidPhone:
    def call(self):
        print("Android call")
class iPhone:
    def call(self):
        print("iPhone call")
def call(x):
    x.call()
a=AndroidPhone()
i=iPhone()
call(a)
call(i)