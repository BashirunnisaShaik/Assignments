try:
    q=int(input("Enter quantity: "))
    if q<=0:
        raise ValueError("Invalid quantity")
    print("Quantity:",q)
except ValueError as e:
    print(e)