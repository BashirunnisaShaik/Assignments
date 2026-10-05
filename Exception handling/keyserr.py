try:
    d={"name":"Bashir","age":18,"course":"CME"}
    k=input("Enter key: ")
    print(d[k])
except ValueError:
    print("Invalid input")
except KeyError:
    print("Key not found")
except TypeError:
    print("Invalid type")