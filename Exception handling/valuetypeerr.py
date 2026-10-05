try:
    a=int(input("Enter number: "))
    b=int(input("Enter number: "))
    print(a/b)
except ValueError:
    print("Invalid value")
except TypeError:
    print("Invalid type")
except ZeroDivisionError:
    print("Cannot divide by zero")