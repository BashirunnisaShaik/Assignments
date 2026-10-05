try:
    n=int(input("Enter number: "))
except ValueError:
    print("Invalid input")
else:
    print("Square:",n*n)