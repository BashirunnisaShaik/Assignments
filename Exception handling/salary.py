try:
    s=float(input("Enter salary: "))
    if s<0:
        raise ValueError("Salary cannot be negative")
    print("Salary:",s)
except ValueError as e:
    print(e)