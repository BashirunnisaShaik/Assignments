try:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    op=input("Enter operator: ")

    if op=="+":
        print(a+b)
    elif op=="-":
        print(a-b)
    elif op=="*":
        print(a*b)
    elif op=="/":
        print(a/b)
    else:
        print("Invalid operator")
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")