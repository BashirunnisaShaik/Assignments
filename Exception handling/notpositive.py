try:
    n=int(input("Enter number: "))
    if n<=0:
        raise ValueError("Number must be positive")
    print(n)
except ValueError as e:
    print(e)