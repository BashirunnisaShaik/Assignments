try:
    a=[10,20,30,40]
    i=int(input("Enter index: "))
    print(a[i])
except ValueError:
    print("Invalid input")
except IndexError:
    print("Index out of range")
except TypeError:
    print("Invalid type")