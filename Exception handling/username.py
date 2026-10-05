try:
    u=input("Enter username: ")
    if u=="":
        raise ValueError("Username cannot be empty")
    print("Username:",u)
except ValueError as e:
    print(e)