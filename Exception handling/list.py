try:
    a=[10,20,30,40,50]
    i=int(input("Enter index: "))
    print(a[i])
except ValueError:
    print("Enter a valid number")
except IndexError:
    print("Invalid index")