try:
    n=int(input("Enter number: "))
    if n<0:
        raise ValueError("Negative number")
    print(n)
except ValueError as e:
    print(e)