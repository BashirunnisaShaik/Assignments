try:
    d={"name":"Bashir","age":18,"course":"CME"}
    k=input("Enter key: ")
    print(d[k])
except KeyError:
    print("Key not found")