try:
    d={"name":"Bashir","age":18}
    print(d["marks"])
except KeyError:
    print("Key not found")