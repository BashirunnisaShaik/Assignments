products={"Laptop":50000,"Mouse":500,"Phone":20000,"Keyboard":1500,"Tablet":8000}
expensive=set()
for product in products:
    if products[product]>5000:
        expensive.add(product)
print(expensive)