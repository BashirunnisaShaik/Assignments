try:
    f=open("data.txt","r")
except FileNotFoundError:
    print("File not found")
else:
    print(f.read())
finally:
    print("File operation complete")