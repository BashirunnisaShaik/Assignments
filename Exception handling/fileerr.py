try:
    f=open("abc.txt","r")
    print(f.read())
except FileNotFoundError:
    print("File not found")