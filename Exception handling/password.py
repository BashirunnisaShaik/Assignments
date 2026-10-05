try:
    p=input("Enter password: ")
    if len(p)<8:
        raise ValueError("Password must contain at least 8 characters")
    print("Valid password")
except ValueError as e:
    print(e)