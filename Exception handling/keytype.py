try:
    d={"name":"Bashir","age":18}
    k=input("Enter key: ")
    print(d[k])
except KeyError:
    print("Key not found")
except TypeError:
    print("Invalid type")