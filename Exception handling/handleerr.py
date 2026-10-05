try:
    f=open("numbers.txt","r")
    for x in f:
        print(int(x))
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Invalid data in file")
except PermissionError:
    print("Permission denied")