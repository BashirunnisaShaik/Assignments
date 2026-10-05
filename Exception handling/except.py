try:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print("Addition:",a+b)
    print("Division:",a/b)
    print("List:",[10,20,30][a])
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
except IndexError:
    print("Index out of range")
except TypeError:
    print("Invalid type")